# Run Prompt — Batch 9 (IT Services / India-UK sponsors), JOBS
#
# Paste below the line into Claude (Chrome extension on, logged into LinkedIn).
# ATTACH companies.csv. Run this in a SEPARATE session from the people search.

---

You are helping me find jobs on LinkedIn using the Claude Chrome extension.
Navigate LinkedIn Jobs directly (I'm already logged in). Do NOT invent anything —
only report postings you actually see. If a field isn't visible, write "not
visible". If you hit a login wall, CAPTCHA, or block, STOP and tell me. Do not
apply, click, or send anything — research only.

## THIS SESSION
Do **Batch 9 only** — JOBS at: Cognizant, TCS, Infosys, Wipro, HCL, Tech Mahindra,
Fujitsu, Atos, Sopra Steria, CGI, DXC Technology, FDM Group, BJSS, Kainos,
Version 1, Endava, GlobalLogic, Softwire, Scott Logic, Thoughtworks.

## MY PROFILE (for fit judgement)
Final-year MSc AI at Brunel (finishing April 2027); 1.5 yrs analytics consulting at
Pythian (SAP HANA, ETL, SQL); skills: SQL, Python, ETL/ELT, Snowflake/dbt/Airflow,
RAG chatbot on AWS, Tableau. Need UK visa sponsorship. Based London / hybrid UK.

## WHAT TO SEARCH
Search LinkedIn Jobs at the companies above for these titles — PRIORITISE junior /
entry-level / experienced-hire over structured grad schemes:
"Junior Data Analyst", "Data Analyst", "Junior Data Engineer", "Data Engineer",
"Junior Data Scientist", "Data Scientist", "Junior AI Engineer", "AI Engineer",
"Junior ML Engineer", "ML Engineer", "Analytics Engineer", "Associate Data",
"Graduate Data" (only if open to 2027 + sponsorship).
Filter location to UK / London / Hybrid. Prefer posts from the last 30 days.

## FOR EACH POSTING capture (into 02_Job_Postings.csv, don't rename columns):
Job Title, Company, Location, Posting URL, Date Posted, Role Type (`Junior role`
or `Grad scheme`), Eligibility Flag, Fit Notes, Referral Contact (leave blank).

Eligibility Flag rules:
- `Eligible` = posting states it sponsors / is open to visa candidates.
- `❌ Not Eligible` = says "must not require sponsorship now or in future", or
  requires security clearance / unrestricted right to work. Mark Status = Skip.
- `Check` = nothing stated — I'll verify.
Do NOT mention sponsorship in any message (N/A here, but keep it tracker-only).

## OUTPUT
Fill 02_Job_Postings.csv. Set Priority 1..N, best-fit junior roles that are
Eligible at the top; push grad schemes and Not-Eligible ones lower.

## WHEN DONE
Short summary: how many postings found, how many are junior vs grad scheme, how
many Eligible vs Not Eligible, and the top 2–3 to apply to first with why.
