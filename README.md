# Job-Hunt MCP Server

A local MCP server for **Claude Desktop** that helps you find hiring managers in London
(via Apollo.io) and send outreach from your Gmail.

## What it does

| Tool | What it does | Cost |
|------|--------------|------|
| `apollo_search_people` | Find hiring managers / recruiters by title + location | **Free** (no email) |
| `apollo_enrich_person` | Reveal a verified email for ONE chosen person | 1 Apollo credit |
| `draft_cold_email` | Build a compliant cold-email draft | Free, no sending |
| `gmail_create_draft` | Save an email to Gmail Drafts (test-safe) | Free |
| `gmail_send_email` | Actually send an email from your Gmail | Free |

Searching is free; emails are revealed only when you explicitly ask, so you won't
burn your ~75–100 free Apollo credits by accident.

---

## Setup (do these in order)

### Step 1 — Install Python deps
```bash
cd job-hunt-mcp
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
# .\venv\Scripts\activate         # Windows PowerShell
pip install -r requirements.txt
```

### Step 2 — Get your Apollo API key
1. Sign up at https://apollo.io (free plan).
2. Go to **Settings → Integrations → API**.
3. Create / copy your API key.

### Step 3 — Set up Gmail API access (OAuth)
1. Go to https://console.cloud.google.com → create a new project.
2. **APIs & Services → Library** → search "Gmail API" → **Enable**.
3. **APIs & Services → OAuth consent screen** → choose **External** →
   fill app name + your email → add yourself under **Test users**.
4. **APIs & Services → Credentials → Create Credentials → OAuth client ID** →
   application type **Desktop app**.
5. **Download JSON**, rename it to `credentials.json`, and put it in this folder.

### Step 4 — Configure secrets
```bash
cp .env.example .env
```
Edit `.env` and fill in `APOLLO_API_KEY`, `SENDER_NAME`, `SENDER_POSTAL_ADDRESS`.

### Step 5 — First-run Gmail auth (one time)
Run the server once from the terminal so the Google login window opens:
```bash
source venv/bin/activate
python server.py          # a browser opens; log in + approve. Creates token.json. Ctrl+C after.
```

### Step 6 — Connect to Claude Desktop
Open Claude Desktop → **Settings → Developer → Edit Config**, and add this
(replace the two paths with your ABSOLUTE paths):

```json
{
  "mcpServers": {
    "job-hunt": {
      "command": "/ABSOLUTE/PATH/job-hunt-mcp/venv/bin/python",
      "args": ["/ABSOLUTE/PATH/job-hunt-mcp/server.py"]
    }
  }
}
```
Config file locations:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Fully **quit and reopen** Claude Desktop. You should see the `job-hunt` tools
appear (hammer/tools icon).

---

## Try it in Claude

> "Search for hiring managers and engineering managers at fintech companies in London."

> "Reveal the email for result #3."

> "Draft a cold email to them for a backend engineer role — my background is 4 years Python/Django."

> "Save that as a Gmail draft so I can review it." (safe)

> "Send it." (real send — Claude will confirm first)

---

## Safety & compliance notes
- **Deliverability:** sending cold email from your primary Gmail can hurt its
  reputation at volume. Keep it low (a handful/day) or switch to draft-only.
- **Legal:** cold email requires a real identity + opt-out (CAN-SPAM / UK PECR /
  GDPR). The `draft_cold_email` tool bakes this into the footer.
- **LinkedIn:** this server does NOT automate LinkedIn — that violates their ToS
  and risks a ban. Use LinkedIn manually for research.
- **Secrets:** `.env`, `credentials.json`, and `token.json` are git-ignored. Never commit them.
