# LinkedIn Networking Kit (for Sara)

A repeatable, safe workflow for finding referrals + grad/junior data/AI roles in the UK.

## Files
| File | What it's for |
|------|---------------|
| `PROMPT_v2.md` | The improved prompt to paste into Claude (Chrome extension) |
| `companies.csv` | Paste your ~300 target companies here (group them into Batches of ~25) |
| `01_People_to_Contact.csv` | Tracker tab 1 — people + draft messages |
| `02_Job_Postings.csv` | Tracker tab 2 — jobs + eligibility flags |
| `03_Company_Notes.csv` | Tracker tab 3 — per-company intel |

## How to use it (the better flow)

1. **Load your companies.** Open `companies.csv`, paste your ~300 firms, and put a
   Batch number (1, 2, 3…) next to each — about 25 per batch.
2. **Run People first.** Paste `PROMPT_v2.md` into Claude, tell it "do Batch 1,
   people only". Review the 15 drafts.
3. **Run Jobs separately** (another session). "Do Batch 1, jobs only."
4. **Review + send yourself.** Claude never sends anything — you review every
   draft and hit send manually in LinkedIn.
5. **Repeat per batch.** Batching keeps you under LinkedIn's rate limits so you
   don't get CAPTCHA'd or restricted.

## Why batches?
LinkedIn blocks accounts that browse too fast. 300 companies in one go = guaranteed
block. ~25 at a time, people and jobs on different days = safe and sustainable.

## The draft-message philosophy
Last version produced 15 near-identical "fellow Brunel alum + RAG chatbot" notes.
v2 fixes this: every message leads with something true about THEM, uses ONE proof
point about you, and makes a clear honest ask. You're job-hunting — owning that
("I'd value your guidance / a referral") beats vague "let's connect" fluff.

## Opening the CSVs as a spreadsheet
Open any `.csv` in Excel or Google Sheets. To combine all three tabs into one
workbook: open a new Google Sheet → File → Import → upload each CSV as a new tab.
