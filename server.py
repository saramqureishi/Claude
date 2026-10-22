"""
Job-Hunt MCP Server
===================
A local MCP server for Claude Desktop that helps with a job search:

  Tools:
    - apollo_search_people : find hiring managers / recruiters (FREE, no emails)
    - apollo_enrich_person : reveal a verified email for one person (costs 1 credit)
    - draft_cold_email     : build a compliant cold-email draft (no sending)
    - gmail_send_email     : send an email from your Gmail (asks Claude to confirm first)
    - gmail_create_draft   : save a draft in Gmail instead of sending (safer)

Credit safety: searching is free. Emails are ONLY revealed when you explicitly
call apollo_enrich_person, so you never burn your tiny free-tier credit pool by accident.
"""

import os
import base64
import json
from email.mime.text import MIMEText

import httpx
from mcp.server.fastmcp import FastMCP

# ---- Config -----------------------------------------------------------------
# We load .env manually (no extra dependency) so secrets stay out of the code.
def _load_dotenv() -> None:
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if not os.path.exists(env_path):
        return
    with open(env_path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()

APOLLO_API_KEY = os.environ.get("APOLLO_API_KEY", "")
SENDER_NAME = os.environ.get("SENDER_NAME", "")
SENDER_POSTAL_ADDRESS = os.environ.get("SENDER_POSTAL_ADDRESS", "")

APOLLO_BASE = "https://api.apollo.io/api/v1"

# Gmail scopes: send + create drafts. Nothing destructive.
GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")

mcp = FastMCP("job-hunt")


# ---- Apollo tools -----------------------------------------------------------
@mcp.tool()
def apollo_search_people(
    job_titles: list[str],
    locations: list[str] | None = None,
    organization_locations: list[str] | None = None,
    keywords: str | None = None,
    per_page: int = 10,
    page: int = 1,
) -> str:
    """Search Apollo's database for people (e.g. hiring managers, recruiters).

    This is FREE and does NOT consume credits. It returns names, titles,
    companies, and LinkedIn URLs — but NOT email addresses. To get an email,
    call apollo_enrich_person on a specific result.

    Args:
        job_titles: Titles to match, e.g. ["Hiring Manager", "Engineering Manager", "Talent Acquisition"].
        locations: Person's own location, e.g. ["London, United Kingdom"].
        organization_locations: Filter by the employer's location instead, e.g. ["London, United Kingdom"].
        keywords: Free-text keywords (company names, skills, etc.).
        per_page: Results per page (max 100).
        page: Page number.
    """
    if not APOLLO_API_KEY:
        return "ERROR: APOLLO_API_KEY is not set. Add it to the .env file."

    payload: dict = {
        "person_titles": job_titles,
        "per_page": min(per_page, 100),
        "page": page,
    }
    if locations:
        payload["person_locations"] = locations
    if organization_locations:
        payload["organization_locations"] = organization_locations
    if keywords:
        payload["q_keywords"] = keywords

    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "x-api-key": APOLLO_API_KEY,
    }

    try:
        resp = httpx.post(
            f"{APOLLO_BASE}/mixed_people/search",
            headers=headers,
            json=payload,
            timeout=30.0,
        )
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        return f"Apollo API error {e.response.status_code}: {e.response.text}"
    except Exception as e:  # noqa: BLE001
        return f"Request failed: {e}"

    data = resp.json()
    people = data.get("people", [])
    total = data.get("pagination", {}).get("total_entries", len(people))

    if not people:
        return "No people found. Try broadening the titles or locations."

    lines = [f"Found {total} total match(es). Showing {len(people)}:\n"]
    for i, p in enumerate(people, 1):
        org = (p.get("organization") or {}).get("name", "—")
        lines.append(
            f"{i}. {p.get('name', '—')} — {p.get('title', '—')} @ {org}\n"
            f"   id: {p.get('id', '—')}\n"
            f"   location: {p.get('city', '—')}, {p.get('country', '—')}\n"
            f"   linkedin: {p.get('linkedin_url', '—')}"
        )
    lines.append(
        "\nNOTE: emails are hidden. To reveal one, call apollo_enrich_person "
        "with the person's id (costs 1 Apollo credit)."
    )
    return "\n".join(lines)


@mcp.tool()
def apollo_enrich_person(
    person_id: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    organization_name: str | None = None,
    domain: str | None = None,
) -> str:
    """Reveal a verified email for ONE person. COSTS 1 APOLLO CREDIT if an email is found.

    Only call this when the user has clearly chosen a specific person to contact.
    Provide either person_id (from a search result) OR name + company/domain.
    """
    if not APOLLO_API_KEY:
        return "ERROR: APOLLO_API_KEY is not set. Add it to the .env file."

    payload: dict = {"reveal_personal_emails": True}
    if person_id:
        payload["id"] = person_id
    if first_name:
        payload["first_name"] = first_name
    if last_name:
        payload["last_name"] = last_name
    if organization_name:
        payload["organization_name"] = organization_name
    if domain:
        payload["domain"] = domain

    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "x-api-key": APOLLO_API_KEY,
    }

    try:
        resp = httpx.post(
            f"{APOLLO_BASE}/people/match",
            headers=headers,
            json=payload,
            timeout=30.0,
        )
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        return f"Apollo API error {e.response.status_code}: {e.response.text}"
    except Exception as e:  # noqa: BLE001
        return f"Request failed: {e}"

    person = resp.json().get("person") or {}
    if not person:
        return "No match found for that person."

    org = (person.get("organization") or {}).get("name", "—")
    return (
        f"Name: {person.get('name', '—')}\n"
        f"Title: {person.get('title', '—')}\n"
        f"Company: {org}\n"
        f"Email: {person.get('email', 'not available')}\n"
        f"LinkedIn: {person.get('linkedin_url', '—')}"
    )


# ---- Email drafting (no network) --------------------------------------------
@mcp.tool()
def draft_cold_email(
    recipient_name: str,
    recipient_company: str,
    role_you_want: str,
    your_background: str,
    tone: str = "warm and concise",
) -> str:
    """Build a compliant cold-email draft to a hiring manager. Does NOT send anything.

    The draft includes a real-identity footer and an opt-out line, which cold
    email legally requires (CAN-SPAM in the US, PECR/GDPR in the UK/EU).
    """
    if not SENDER_NAME:
        return "ERROR: SENDER_NAME is not set in .env — required for a compliant footer."

    footer = (
        f"\n\n—\n{SENDER_NAME}\n"
        f"{SENDER_POSTAL_ADDRESS}\n"
        f"If you'd prefer not to hear from me, just reply 'no thanks' and I won't follow up."
    )
    guidance = (
        f"Write a {tone} cold email to {recipient_name} at {recipient_company}.\n"
        f"Goal: express interest in a {role_you_want} role.\n"
        f"My background: {your_background}\n\n"
        "Rules: keep it under 150 words, one specific reason you're interested in "
        "THEIR company, one clear ask (a short call), no generic flattery. "
        "Then append exactly this footer:\n"
        f"{footer}"
    )
    return guidance


# ---- Gmail tools ------------------------------------------------------------
def _get_gmail_service():
    """Build an authenticated Gmail client, running the OAuth flow if needed."""
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, GMAIL_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(
                    "credentials.json not found. Download OAuth client credentials "
                    "from Google Cloud Console and save them here."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, GMAIL_SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w", encoding="utf-8") as fh:
            fh.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


def _build_raw_message(to: str, subject: str, body: str) -> dict:
    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}


@mcp.tool()
def gmail_send_email(to: str, subject: str, body: str) -> str:
    """Send an email from your Gmail account. IMPORTANT: confirm with the user before calling.

    This actually sends a real email. Prefer gmail_create_draft while testing.
    """
    try:
        service = _get_gmail_service()
        sent = service.users().messages().send(
            userId="me", body=_build_raw_message(to, subject, body)
        ).execute()
        return f"Email sent to {to}. Message id: {sent.get('id')}"
    except Exception as e:  # noqa: BLE001
        return f"Failed to send: {e}"


@mcp.tool()
def gmail_create_draft(to: str, subject: str, body: str) -> str:
    """Save an email as a Gmail draft WITHOUT sending it. Safe for testing."""
    try:
        service = _get_gmail_service()
        draft = service.users().drafts().create(
            userId="me", body={"message": _build_raw_message(to, subject, body)}
        ).execute()
        return f"Draft saved in Gmail (id: {draft.get('id')}). Review it in your Drafts folder."
    except Exception as e:  # noqa: BLE001
        return f"Failed to create draft: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
