# PROMPT — Full company audit: find current grad/junior roles across my list
#
# Goal: go through my target companies (NON-banking) and tell me, for each, whether
# there's a current graduate/junior data/AI role — so I can see what I've missed.
# Attach: sara_background.md, companies.csv, application_tracker.csv
# Run in BATCHES (the companies.csv Batch column) so it's manageable and accurate.

---

You're helping me do a thorough audit of my target companies to find current
graduate/junior roles I can apply to. Read the three attached files first:
- sara_background.md — who I am, my lane, my hard blockers (follow its RULES).
- companies.csv — my 523 target companies (Sector + Batch columns).
- application_tracker.csv — companies I've already applied to and the outcome.

## THIS RUN
Do Batch [N] only (tell me if I didn't specify — default to the lowest batch not
yet audited). List the companies in that batch, then work through them.

## HARD EXCLUSIONS
- EXCLUDE all banking & investment banking. Skip every company whose Sector is
  "Banking & Investment Banking". I cannot work in a bank.
- Skip my hard blockers from sara_background.md (British citizenship, SC/DV
  clearance, "no sponsorship ever", defence/aerospace/gov like BAE, MBDA, etc.).
- Skip companies already in application_tracker.csv with Outcome = Rejected (don't
  re-suggest roles I've been rejected from), but DO note if they have a NEW role.

## WHAT I'M LOOKING FOR
Graduate / junior Data Analyst, Data Engineer, Data Scientist, AI & Data Consultant,
analytics, junior AI/ML Engineer. UK (London/hybrid). 2027 start or rolling junior.
Prioritise employers that SPONSOR Skilled Worker visas. Avoid hardcore SWE,
quant/HFT, PhD-level research, live-coding-heavy roles, actuarial/accountancy
tracks, apprenticeships.

## FOR EACH COMPANY IN THE BATCH, report:
Company | Grad/Junior role found? (Yes/No/Couldn't check) | Role Title(s) & URL |
Location | Sponsorship signal (if visible) | Fit (High/Med/Low) | Notes.
If No role is live, say so plainly ("no current grad/junior data role found") so I
know it's checked, not missed.

## RULES
- Only list REAL postings with working URLs that you actually found via web search
  or the company careers page. Do NOT invent roles. If you can't verify, say
  "couldn't check" — never pad the list.
- Keep my facts honest per sara_background.md (never mention visa in any message;
  this audit's sponsorship notes are for my eyes only).

## OUTPUT
A table for the batch (above columns), then a short summary:
- how many companies had a live grad/junior role,
- which 3 are the best-fit to apply to first and why,
- which companies you couldn't check (so I can check manually).
