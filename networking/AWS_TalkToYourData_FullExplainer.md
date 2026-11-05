# AWS Workshop — Full Explainer ("Talk to Your Data")
**A long-form walkthrough you can read or talk from for 15-20 minutes.**
Date: 5 November 2026 | AWS, 60 Holborn Viaduct, London | Full-day hands-on lab.

This document explains the whole day from scratch: the problem it solves, every concept and tool,
what we actually built, and how it connects to the Snowflake work I already know. It's written so I
can explain it to someone over 15-20 minutes, building up from simple ideas to the technical detail.

---

## 1. THE PROBLEM THE WHOLE DAY IS SOLVING

Start with the pain point, because everything else is a solution to it.

In most companies, data lives in lots of systems, and to get an answer you rely on **dashboards**: fixed
charts and reports that someone on a data team built in advance. That works until you have a NEW question
the dashboard wasn't built for. Then you have to raise a request, wait in a queue, and an analyst writes
some SQL and builds you a new chart. By the time you get the answer, the moment may have passed.

This is called the **"BI bottleneck"** (BI = Business Intelligence). The dashboards can't "talk back" to
you; they just show what they were told to show.

The vision for the day was **conversational analytics**: instead of waiting for someone to build a chart,
you simply ask your data a question in plain English, like *"which region had the highest sales last
quarter?"*, and an AI assistant figures out the query, runs it, and gives you the answer or chart
straight away. The human asks in natural language; the AI does the technical part.

But, and this is the important twist, you can't just point an AI at all your company data and let anyone
ask anything. You need **governance**: control over who can see what, a record of where data came from,
and confidence the answers are trustworthy. So the full title is "AI-Powered Analytics GOVERNED BY YOUR
BUSINESS CONTEXT". Governance is the thread running through the whole day.

---

## 2. THE BIG PICTURE: THE "STACK" (how the pieces fit)

Think of it as a pipeline with layers, from the raw data at the bottom to the human at the top. Data
flows UP; a question flows DOWN and the answer comes back UP.

1. **Storage (bottom):** all raw data lands in **Amazon S3**, which is just cloud storage, like a giant
   hard drive in the cloud holding files (CSV, JSON, Parquet, etc.).
2. **Table format:** raw files are messy, so we lay **Apache Iceberg** on top to turn them into proper,
   query-ready tables, organised into clean layers (bronze, silver, gold).
3. **Query engines:** to actually ask questions of those tables we use **Amazon Athena** (runs SQL
   directly on the files) or **Amazon Redshift** (a full data warehouse for heavier work).
4. **BI / dashboard layer:** **Amazon Quick** (the new name/version of QuickSight) builds dashboards and
   visuals, like Power BI or Tableau. It has **SPICE**, an in-memory cache that makes dashboards fast.
5. **AI layer:** on top we connect an **AI chat agent** through **MCP (Model Context Protocol)**, so you
   can ask questions in natural language and the agent writes the SQL for you.
6. **Governance (wraps everything):** **AWS Lake Formation** and the **Glue Data Catalog** control access
   (even down to specific columns), keep a catalogue of all the data, and track lineage (where data came
   from and what happened to it).

One sentence to hold it all: *"Raw data in S3 becomes clean Iceberg tables, Athena or Redshift query
them, Amazon Quick shows them, an AI agent via MCP lets you ask in plain English, and Lake Formation
governs who can see what, all the way through."*

---

## 3. EACH CONCEPT EXPLAINED PROPERLY (with analogies)

### Amazon S3 (storage)
The simplest piece. It's cloud storage where files live. Think of it as an enormous, cheap, reliable
folder in the cloud. On its own it's just files sitting there; it doesn't know they're "tables" yet.

### Apache Iceberg (the open table format) — this is a star of the day
Raw files in S3 are like loose pages scattered in a box. **Iceberg is the system that organises those
pages into a proper book with a contents page**, so tools can treat them as a real database table: run
SQL, update rows, add new data, and even look at past versions ("time travel").

Two things made Iceberg a big theme:
- It's **open**. It isn't owned by AWS or anyone. So the SAME data can be read by many different tools
  (Athena, Redshift, Snowflake, Spark). You store the data ONCE and avoid being locked into one vendor.
  The slide called this "data portability avoids vendor lock-in by design."
- It supports **bronze/silver/gold** layering:
  - **Bronze** = raw data, as it arrived.
  - **Silver** = cleaned and standardised.
  - **Gold** = business-ready tables people actually report on.
  This is exactly the "staging -> intermediate -> mart" idea from dbt.

### Amazon Athena vs Amazon Redshift (the query engines) — the "Price, Performance & Patterns" session
Both let you run SQL, but they suit different situations, and choosing between them is about cost and
speed.
- **Athena** = "serverless" SQL directly on files in S3. You don't run any server; you just send a query
  and pay per query. Great for occasional or ad-hoc questions. Like paying for a taxi only when you ride.
- **Redshift** = a full data warehouse you provision (it's running and ready). Faster for heavy, frequent,
  complex queries with lots of users at once ("sub-second concurrency", "materialized views"). Like
  owning a car, costs more to keep running, but it's there and fast when you need it a lot.
- The trade-off: **serverless (pay-per-query) vs provisioned (always-on)**, driven by how often you query,
  how complex it is, and how many people hit it at once. You pick based on "query patterns" and cost.

### SPICE (speed)
QuickSight/Quick has an in-memory engine called **SPICE**. It caches a copy of the data in fast memory so
dashboards load instantly instead of re-querying the source every time. Think of it as keeping your most-
used data "warm and ready" so charts pop up immediately. In the lab we saw three stages: query raw S3
directly, then optimise with Iceberg + pre-aggregation, then accelerate with SPICE, each step faster.

### Amazon Quick / QuickSight (the BI layer)
AWS's dashboard and reporting tool, the equivalent of Power BI or Tableau. You connect it to your data,
build charts and dashboards, and share them. The new, exciting part is the **chat agent / natural-language
("Q")** capability: you type a question and it answers with the right chart.

### MCP — Model Context Protocol (the AI bridge)
This is the genuinely new concept. For an AI assistant to answer questions about YOUR data, it needs a
safe, structured way to connect to your data and tools. **MCP is that bridge/translator.** It lets the AI
agent understand what data exists, what it's allowed to touch, and how to query it. Without MCP, the AI is
just a chatbot with no access to your actual numbers; with MCP, it can safely fetch real answers.

### AI chat agents / Topics / Spaces
In Quick, a **Topic** is a curated set of data and definitions you point the AI at (so it understands your
business terms). A **Space** is a shared workspace. A **chat agent** is the thing you actually talk to:
you ask a question, it uses the Topic + MCP to generate the query and reply. We also saw "Flows" for
automating steps and "Scheduled Agents" that run on a timer (e.g. a morning briefing).

### Governance: Lake Formation + Glue Data Catalog — the "Trust" session
The most important idea for responsible AI analytics. Before you let an AI answer questions on company
data, you must guarantee it respects the rules:
- **Access control** (Lake Formation): who can see which tables, down to specific COLUMNS. So an AI
  answering a question for one user won't reveal data that user isn't allowed to see.
- **Glue Data Catalog:** a catalogue/index of all your data, so tools (and the AI) know what exists.
- **Lineage, quality, auditability:** tracking where data came from, whether it's trustworthy, and being
  able to audit what the AI did. If the AI gives an answer, you can check how it got there.
This is why the day's title says "governed by your business context": the AI must operate inside your
company's rules, not freely.

---

## 4. WHAT WE ACTUALLY BUILT IN THE LAB (the hands-on part)

The afternoon was guided, module by module, in AWS sandbox accounts they provided. We worked through:

**A) Set up Amazon Quick and modernise BI**
- Loaded data, configured a data source, built interactive dashboards.
- Created "Quick Spaces" (shared workspaces) and "Quick chat agents" (the AI you ask questions).

**B) AWS MCP Integration**
- Set up the MCP connection, loaded data, then did "natural language exploration", literally asking the
  data questions in English and watching the agent answer.

**C) Agentic AI Analytics with Athena + Quick**
- Prepared data in a data lake, built a dataset and a "Topic" in Quick, built and published a dashboard,
  then added an AI chat agent and interacted with it.

**D) Hospital Operations BI with Redshift + Quick**
- Prepared a Redshift warehouse, connected Quick to it, built an operations dashboard, created Topics and
  a Space, built an operations AI agent, and automated steps with "Flows". (A realistic healthcare use
  case: admissions, operational KPIs, etc.)

**E) Athena Direct Query to SPICE**
- Stage 1: direct SQL query on RAW data in S3, and a dashboard on it.
- Stage 2: optimised with Iceberg tables + pre-aggregation (faster, cheaper).
- Stage 3: accelerated selected data with SPICE (instant dashboards).
- Also queried S3 tables directly from Quick.
- This module nicely showed the SAME data getting progressively faster as you add Iceberg and SPICE.

---

## 5. HOW IT ALL CONNECTS TO WHAT I ALREADY KNOW (Snowflake)

This is my honest anchor, and a strong thing to say to AWS people.

In my own time I built a modern data-engineering project on **Snowflake** with **dbt** and **Airflow**:
- Loaded raw files into Snowflake.
- Used dbt to transform them into layered models, staging -> intermediate -> mart, which is exactly
  **bronze/silver/gold**.
- Scheduled and orchestrated the pipeline with Airflow.

So today mapped almost one-to-one onto that:
- Raw files in S3 = the raw landing data I loaded into Snowflake.
- Iceberg tables + bronze/silver/gold = my dbt staging/intermediate/mart layering.
- Athena/Redshift = the query engine (Snowflake's compute in my project).
- Amazon Quick = the dashboard layer (I've used Power BI/Tableau/Plotly).
- Choosing Athena vs Redshift on cost/performance = sizing Snowflake warehouses up/down for cost.
- Governance/access control = Snowflake roles and data validation/quality work.

The genuinely NEW things I learned today were: **Iceberg as an open, portable table format**, the
**Athena-vs-Redshift serverless-vs-provisioned trade-off**, **SPICE** for acceleration, and the **AI/MCP
layer** that turns all of this into natural-language "conversational analytics". The data-engineering
foundations underneath were familiar, which is why I could follow a Level 200-300 lab comfortably.

---

## 6. MY KEY TAKEAWAYS (the points worth repeating)
1. Conversational analytics removes the BI bottleneck: ask in plain English, the AI writes the SQL.
2. Iceberg gives open, portable, layered (bronze/silver/gold) tables and avoids vendor lock-in.
3. Athena vs Redshift is a cost/performance choice: serverless-per-query vs always-on warehouse.
4. SPICE caches data in memory so dashboards are instant.
5. MCP is the bridge that lets an AI agent safely query your real data.
6. Governance (Lake Formation + Glue) is the PREREQUISITE for trusting AI on data: access control,
   lineage, auditability. The AI must operate inside the business's rules.
7. The underlying pattern is the same modern data stack I know from Snowflake/dbt/Airflow, with an AI
   natural-language layer added on top.

---

## 7. HOW TO PITCH IT IN CONVERSATION (quick levels)
- **One line:** "A hands-on AWS lab on conversational analytics, building a governed pipeline where you
  ask your data questions in plain English instead of writing SQL."
- **Non-technical:** "It's about turning dashboards into something you can chat with, you type a question
  and the AI finds the answer, with controls so it only shows data you're allowed to see."
- **Technical:** "End-to-end stack: S3 -> Iceberg (bronze/silver/gold) -> Athena/Redshift -> Amazon Quick
  with SPICE, plus AI chat agents via MCP, governed throughout by Lake Formation. Same pattern as the
  Snowflake/dbt stack I've built, with a natural-language layer on top."
