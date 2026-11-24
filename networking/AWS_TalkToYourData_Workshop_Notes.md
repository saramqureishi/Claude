# AWS Workshop Notes — "Talk to Your Data: AI-Powered Analytics Governed by Your Business Context"
**Date:** 5 November 2026 | **Venue:** AWS, 60 Holborn Viaduct, London | Full-day hands-on lab
**Theme:** Moving from static dashboards to conversational analytics (asking your data questions in plain English) on AWS.

> HOW TO USE: If anyone asks "what did you do at the AWS workshop?", read the summary below.
> Two explanation levels included: one for non-technical people, one for an average technical person.

---

## WHAT WE ACTUALLY DID (the lab modules)

**Setup & Amazon Quick (QuickSight)**
- Set up Amazon Quick (AWS's BI/dashboard tool, like Power BI/Tableau).
- Loaded data, configured a data source, built interactive dashboards.
- Created "Quick Spaces" and "Quick chat agents" (AI agents you ask questions in natural language).
- Explored Quick Desktop.

**AWS MCP Integration**
- Set up AWS MCP (Model Context Protocol) — the bridge that lets an AI assistant connect to your data/tools.
- Loaded data and did natural-language exploration (asking the data questions in English).

**Agentic AI Analytics with Athena + Quick**
- Prepared data in a data lake, built a dataset and "Topic" in Quick, built and published a dashboard.
- Added an AI chat agent and interacted with it (asked it questions).

**Hospital Operations BI with Quick (Redshift)**
- Prepared an Amazon Redshift warehouse, connected Quick to it.
- Built an operations dashboard, created Topics and a Space, built an operations AI agent, automated with Flows.

**Athena Direct Query to SPICE with Quick**
- Stage 1: direct SQL query on raw data in S3, built a dashboard on it.
- Stage 2: optimised with Iceberg tables + pre-aggregation.
- Stage 3: accelerated data using SPICE (QuickSight's fast in-memory cache).
- Queried S3 tables directly from Quick.

---

## THE TOOLS (one line each)
- **Amazon Quick / QuickSight** = AWS's dashboard/BI tool (like Power BI). "Q" = ask questions in plain English.
- **Amazon Athena** = run SQL directly on files in S3 storage, pay per query.
- **Amazon Redshift** = AWS's data warehouse, for heavy/fast repeated queries.
- **Apache Iceberg** = open table format that turns raw files into clean, query-ready tables (bronze/silver/gold).
- **Amazon S3** = cloud storage for raw files.
- **SPICE** = QuickSight's fast in-memory engine that caches data so dashboards load instantly.
- **MCP (Model Context Protocol)** = the bridge that lets an AI assistant safely talk to your data.
- **AI chat agent / Topic** = the conversational layer you ask questions to, in natural language.

---

## THE ONE-SENTENCE SUMMARY
"It was a hands-on AWS lab on conversational analytics: we built pipelines where raw data in S3 becomes
clean Iceberg tables, gets queried by Athena or Redshift, and is shown in Amazon Quick dashboards, then
we added AI chat agents (via MCP) so you can ask the data questions in plain English instead of writing SQL."

---

## IF SOMEONE ASKS "WHAT IS THAT?" — NON-TECHNICAL VERSION
"You know how normally a company has dashboards, like fixed charts someone built, and if you want a
different answer you have to ask an analyst and wait? This was about letting people just TYPE a question
in plain English, like 'which hospital had the most admissions last month?', and the computer finds the
answer itself. We spent the day building the behind-the-scenes setup that makes that possible, and making
sure it's safe, so the AI only shows people the data they're allowed to see."

Everyday analogy: "It's like turning a pile of messy spreadsheets into something you can just chat with,
like texting a question and getting the chart back, instead of building the chart yourself."

---

## IF SOMEONE ASKS "WHAT IS THAT?" — AVERAGE TECHNICAL VERSION
"It's an end-to-end conversational analytics stack on AWS. Raw data lands in S3, we structure it as
Apache Iceberg tables in a bronze/silver/gold layout, and query it with Athena (serverless SQL on S3)
or Redshift (warehouse) depending on the workload. The BI layer is Amazon Quick (QuickSight), with SPICE
for in-memory acceleration. On top we added AI chat agents connected through MCP, so you query in natural
language and the agent generates the SQL. Governance runs throughout via Lake Formation, so access control
and data policy are enforced even when the AI is the one querying."

Snowflake comparison (my honest angle): "It's basically the same modern-data-stack pattern I built in
Snowflake with dbt and Airflow — raw to staging to mart, i.e. bronze/silver/gold — just with AWS tools
(Iceberg + Athena/Redshift + Quick) and an AI/natural-language layer on top."

---

## MY KEY TAKEAWAYS (what I learned / can talk about)
1. Conversational analytics = ask data questions in plain English; the AI writes the query.
2. Iceberg gives you open, portable tables (no vendor lock-in) with bronze/silver/gold layering.
3. Athena vs Redshift = serverless-per-query vs provisioned warehouse; choose by cost + query pattern.
4. SPICE accelerates dashboards by caching data in memory.
5. Governance (Lake Formation) is the prerequisite for trusting AI on your data — access control, lineage, policy.
6. MCP is the bridge connecting the AI agent to the data safely.
