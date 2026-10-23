# LinkedIn Networking Prompt v2 — paste into Claude (with Chrome extension)

> Run People-search and Jobs-search as SEPARATE sessions (don't do both at once —
> fewer page loads = lower chance LinkedIn blocks you). Do ONE batch of ~25
> companies per session from companies.csv.

---

You are helping me network on LinkedIn using the Claude Chrome extension. Navigate
LinkedIn directly (I'm already logged in). **Do not guess or invent anything —
only report people, posts, and jobs you actually see on the page.** If a field
isn't visible, write "not visible" rather than filling it in.

## MY GOAL
Find (1) people for warm networking / referrals and (2) open job postings, for
graduate & junior data/AI roles in the UK. Prioritise warm-intro paths (shared
school/employer/background).

## MY BACKGROUND
- Name: Sara Qureishi
- Current: Final-year MSc Artificial Intelligence, Brunel University London (finishing ~April 2027)
- Prior: ~1.5 yrs Graduate Analytics Consultant at Pythian (SAP HANA migration, ETL, SQL; promoted in 4 months)
- Looking for: Graduate/junior roles (2027 start or rolling) in data analytics, data
  engineering, data science, applied AI, AI/ML engineering — London or hybrid UK.
- Top skills: SQL, Python, ETL/ELT, data modelling (Snowflake/dbt/Airflow), a
  RAG chatbot built on AWS, Tableau, client-facing consulting.

## TARGET CRITERIA
- Companies: use the list I provide in companies.csv (523 companies, grouped into
  23 Batches). Work through ONE "Batch" per session. The `Flag` column means:
  blank = fine; `CHECK` = may need clearance/residency, verify before applying;
  `NOT ELIGIBLE` = requires UK citizenship/clearance — SKIP for jobs, but a data
  person there can still be worth a networking chat.
- Roles — PRIORITISE junior / entry-level / experienced-hire roles OVER structured
  graduate schemes. Reason: grad schemes are blind applications that can't be
  referred, whereas junior team roles CAN be referred and suit me well. Search these
  titles: "Junior Data Analyst", "Data Analyst", "Junior Data Engineer", "Data
  Engineer", "Junior Data Scientist", "Data Scientist", "Junior AI Engineer", "AI
  Engineer", "Junior ML Engineer", "ML Engineer", "Analytics Engineer", "Associate
  Data ...", "Entry level data". Only include grad schemes if clearly open to
  2027 + visa sponsorship. Tag each job in the tracker as `Junior role` or
  `Grad scheme` so I can tell them apart.
- SECTOR FOCUS for this run: do NOT concentrate on banking. If I ask for a specific
  Batch, use it. Otherwise prioritise non-banking sectors (Tech & AI, IT services /
  India-UK sponsors, Pharma, FMCG, Retail) where I have strong skill matches.
- People to contact — aim for this MIX out of 15 (hard rules):
  - MAX 3 recruiters / early-careers TA.
  - Prioritise: (a) recent grads (1st–2nd yr) now IN these roles, (b) hiring
    managers / team leads / data managers, (c) directors/VPs where reachable.
  - Prioritise 1st-degree, then 2nd-degree with a named mutual.
- Shared background to actively filter for (higher reply rates), using LinkedIn's
  REAL filters, not keyword text:
  - School filter = Brunel University London
  - Past company filter = Pythian
  - School/Location filter = universities in India / Hyderabad / India region
    (use the School and Past-Location filters, not free-text keywords)

## ELIGIBILITY (important)
I need UK visa sponsorship. For JOBS: flag each as `Eligible`, `Check`, or
`❌ Not Eligible`. Mark `❌ Not Eligible` if it requires security clearance
(SC/DV) or an "unrestricted right to work". **Do NOT mention visa sponsorship in
any outreach draft** — that's for my eyes only, in the tracker.

## WHAT TO DO
1. Use LinkedIn native People search, Jobs search, and company employee lists +
   filters (location UK/London; school; past company; connection degree).
2. PEOPLE: pull up to 15 relevant profiles. For each capture: Name, Title,
   Company, Location, LinkedIn URL, Connection Degree, Mutual Connections, Shared
   Background, and 1–2 lines on why they fit. Where a 1st-degree connection could
   introduce me to a 2nd-degree target, note the **Intro Path** (who → whom).
3. JOBS: search with my criteria; for each posting capture Job Title, Company,
   Location, URL, Date Posted, Eligibility Flag (above), and a 1–2 line fit note.
4. If you hit a login wall, CAPTCHA, or any block — STOP and tell me. Do not work around it.
5. Do NOT send requests, messages, InMails, Connect or Follow. Research + draft only.

## OUTPUT — fill the CSV templates
Fill these files (same columns, don't change headers):
- 01_People_to_Contact.csv
- 02_Job_Postings.csv
- 03_Company_Notes.csv
Sort best-fit / highest-priority to the top (set the Priority column 1..N).

## DRAFT MESSAGES — read carefully, this is where quality matters
For each person, write a draft under 400 characters in the Draft Message column.
Also set a `Message Type` per person and match the ask to who they are:

- **Advice** (recent grads, peers): ask for 2–3 specific questions / how they
  broke in. Low pressure, honest: "genuinely trying to learn from someone who did it."
- **Team-hiring** (hiring managers, team leads): ask directly if their team takes
  grads/juniors for 2027, and what they rate in candidates. Offer to share CV.
- **Referral** (1st-degree / warm contacts only): be most direct — ask them to
  point me to early-careers contact or flag my CV internally.

HARD RULES for drafts (this is what was wrong last time — fix it):
1. Lead with something SPECIFIC and TRUE about THEM (their actual role, team,
   a recent post, or a genuine shared point) — NOT a reused opener.
2. Do NOT start more than ~3 messages with "As a fellow Brunel alum". Vary openers.
3. ONE proof point about me max. Do NOT recite my whole CV. In particular, do NOT
   mention "RAG chatbot on AWS" in more than ~2 messages total.
4. Make the ask CLEAR and HONEST. I AM job-hunting for referrals/guidance — don't
   hide that behind vague "I'd love to connect / swap notes." Honesty > fake politeness.
5. Each of the 15 must read differently. If two drafts feel interchangeable, rewrite one.
6. Never mention visa/sponsorship.
7. Tone: warm, genuine, direct. Human, not corporate.

## WHEN DONE
Give a short summary: how many people/jobs found, which filters limited results,
and the 2–3 people/jobs you'd prioritise first and why (especially any strong Intro Paths).
