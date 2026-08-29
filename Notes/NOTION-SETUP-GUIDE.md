# Notion setup guide — Yacoub's DevOps learning management system

This turns `Yacoub_Notion_Tasks.csv` (360 tasks across 61 days) into a working system.
Setup takes about 30 minutes once. After that the daily routine is five clicks.

---

## Part 1 — Import the CSV

1. Open Notion. In the left sidebar, hover over your workspace name and click **+** to
   create a new blank page. Call it **Yacoub DevOps Programme**.
2. On the empty page, type `/import` and choose **Import**.
3. Choose **CSV**, then select `Yacoub_Notion_Tasks.csv`.
4. Notion creates a new database with 360 rows. This takes a minute or two — let it finish.
5. Rename the database to **DevOps Tasks** (click the title at the top).

> If you are on mobile, do the import on a laptop. Notion's mobile app cannot import CSVs.
> Everything afterwards works fine on mobile.

---

## Part 2 — Fix the property types

Notion imports every column as plain **Text**. Five of them need changing or the views and
dashboard will not work. Click each column header → **Edit property** → change **Type**.

| Column | Change type to | Then do this |
|---|---|---|
| `Date` | **Date** | Notion will parse the `2026-09-07` format automatically |
| `Status` | **Select** | Add options in this order: `Not Started`, `In Progress`, `Blocked`, `Done`. Colour them grey, blue, red, green. |
| `Category` | **Select** | Options: `Udemy`, `Tech365`, `Practice`, `Lab`, `Project`, `GitHub`, `LinkedIn`, `Presentation`, `Revision`, `Capstone` |
| `Priority` | **Select** | Options: `High`, `Medium`, `Low` |
| `Week` | **Select** | Options `Week 1` through `Week 9` |
| `GitHub Required` | **Select** | Options: `Yes`, `No` |
| `LinkedIn Required` | **Select** | Options: `Yes`, `No` |
| `Lab Required` | **Select** | Options: `Yes`, `No` |
| `Presentation Required` | **Select** | Options: `Yes`, `No` |
| `GitHub Evidence` | **URL** | Yacoub pastes commit links here |
| `LinkedIn URL` | **URL** | Yacoub pastes post links here |

Leave `Task`, `Start Time`, `End Time`, `Course Section`, `Lecture Numbers`,
`Lecture Titles`, `Task Description`, `Deliverable`, `Estimated Duration` and `Notes`
as **Text**.

**Tip:** when you change a column to Select, Notion offers to create the options from the
existing values automatically. Accept that — it saves typing.

---

## Part 3 — Add two formula properties

These power the dashboard. Click **+** at the far right of the columns → **Formula**.

**Property name: `Done?`** (used for all progress bars)
```
if(prop("Status") == "Done", 1, 0)
```

**Property name: `Is Today`** (optional, makes the TODAY view simpler)
```
if(formatDate(prop("Date"), "YYYY-MM-DD") == formatDate(now(), "YYYY-MM-DD"), true, false)
```

---

## Part 4 — Create the ten views

At the top of the database, click **+ New view** for each. Set the **filter** and **sort**
as shown, then rename the view.

### 1. TODAY  ← this is the one Yacoub opens every morning
- Layout: **Table**
- Filter: `Date` → **Is** → **Today**
- Sort: `Start Time` → Ascending
- Hide properties: everything except `Task`, `Start Time`, `Category`, `Status`,
  `Lecture Numbers`, `GitHub Evidence`, `LinkedIn URL`, `Notes`
- **Drag this view to first position.** It should be the default.

### 2. THIS WEEK
- Layout: **Table**, grouped by `Day`
- Filter: `Date` → **Is within** → **The current week**
- Sort: `Date` Ascending, then `Start Time` Ascending

### 3. BOARD
- Layout: **Board**
- Group by: `Status`
- Filter: `Date` → **Is within** → **The current week** (otherwise 360 cards is unusable)
- Card preview: none; show `Date`, `Category`, `Priority`

### 4. CALENDAR
- Layout: **Calendar**
- Date property: `Date`
- Show properties on cards: `Task`, `Category`

### 5. SATURDAY LABS
- Layout: **Table**
- Filter: `Category` → **Is** → `Lab`
- Sort: `Date` Ascending

### 6. SUNDAY PRESENTATIONS
- Layout: **Table**
- Filter: `Category` → **Is** → `Presentation`
- Sort: `Date` Ascending

### 7. LINKEDIN
- Layout: **Table**
- Filter: `LinkedIn Required` → **Is** → `Yes`
- Sort: `Date` Ascending
- Show `LinkedIn URL` prominently — an empty cell means a missed post

### 8. GITHUB
- Layout: **Table**
- Filter: `GitHub Required` → **Is** → `Yes`
- Sort: `Date` Ascending
- Show `GitHub Evidence` prominently

### 9. BLOCKED  ← the view Ade checks
- Layout: **Table**
- Filter: `Status` → **Is** → `Blocked`
- Sort: `Date` Ascending
- Show `Notes` — this is where Yacoub explains what he is stuck on

### 10. COMPLETED
- Layout: **Table**
- Filter: `Status` → **Is** → `Done`
- Sort: `Date` Descending

---

## Part 5 — Yacoub's daily routine

This is the whole system from his side. Seven steps, most days under a minute of admin.

1. Open **TODAY**.
2. Read the tasks top to bottom — they are already in time order.
3. Start the first one, set `Status` → **In Progress**.
4. When finished, set `Status` → **Done**.
5. If `GitHub Required` is Yes, paste the commit URL into `GitHub Evidence`.
6. If `LinkedIn Required` is Yes, paste the post URL into `LinkedIn URL`.
7. If something went wrong or he got stuck, write it in `Notes` and set `Status` →
   **Blocked**.

**The Blocked status is the important one.** It is not an admission of failure — it is the
signal that Ade should look. Being stuck for two hours and saying nothing is the failure.

---

## Part 6 — Remote monitoring (Ade)

1. On the **Yacoub DevOps Programme** page, click **Share** → **Invite** → enter Ade's
   email → permission **Can edit** (or **Can comment** if you prefer read-only oversight).
2. Ade opens the same workspace and uses these views:
   - **BLOCKED** — is he stuck on anything right now?
   - **THIS WEEK** — how much of the week is still `Not Started` on a Thursday?
   - **GITHUB** and **LINKEDIN** — are the evidence columns actually being filled in?
     Empty URL cells on past dates are the earliest warning sign that the habit is slipping.
   - **COMPLETED** — sorted newest first, this is the activity feed.
3. Notion sends notifications on comments. Comment directly on a task row rather than
   messaging separately — the context stays attached to the work.

---

## Part 7 — Build the dashboard

Create a new page inside **Yacoub DevOps Programme** called **Dashboard**. Add these
blocks. Every number updates itself — no manual admin.

### Method: linked database views with rollups

For each metric below, type `/linked` on the Dashboard page, choose **Linked view of
database**, select **DevOps Tasks**, then set the filter and switch the layout so it shows
a count.

To display a count rather than rows: open the linked view → **...** menu → turn on
**Calculate** at the bottom of the table → choose **Count all** (or **Percent checked**
where noted).

| Dashboard metric | Linked view filter | Calculation |
|---|---|---|
| **Overall course progress** | *(no filter — all 360 tasks)* | Bottom bar → `Done?` → **Sum**, next to a Count all. Or `Status` → **Percent per group** |
| **Weekly progress** | `Date` is within **the current week** | `Status` → **Percent per group**, shows the Done share of this week |
| **Labs completed** | `Category` is `Lab` **AND** `Status` is `Done` | **Count all** (out of 47 lab tasks) |
| **Projects completed** | `Category` is `Capstone` or `Project` | **Count all** where Status is Done (4 total) |
| **GitHub updates** | `GitHub Required` is `Yes` **AND** `GitHub Evidence` **is not empty** | **Count all** (target: 63) |
| **LinkedIn reports** | `LinkedIn Required` is `Yes` **AND** `LinkedIn URL` **is not empty** | **Count all** (target: 61) |
| **Tasks completed** | `Status` is `Done` | **Count all** |
| **Tasks remaining** | `Status` is **not** `Done` | **Count all** |
| **Blocked tasks** | `Status` is `Blocked` | **Count all** — put this one at the top in red |

### Layout suggestion

Use `/columns` to create a 3-column layout:

```
┌─────────────────────┬─────────────────────┬─────────────────────┐
│ BLOCKED (red)       │ Overall progress    │ Weekly progress     │
├─────────────────────┼─────────────────────┼─────────────────────┤
│ Tasks completed     │ Tasks remaining     │ Labs completed      │
├─────────────────────┼─────────────────────┼─────────────────────┤
│ GitHub updates      │ LinkedIn reports    │ Projects completed  │
└─────────────────────┴─────────────────────┴─────────────────────┘
```

Then embed the **TODAY** view full-width underneath, so the dashboard doubles as the
daily start page.

### Milestone checklist

Add a simple to-do list at the bottom of the Dashboard with the nine weekly milestones:

- [ ] Week 1 — A multi-tier application running on AWS he built and can explain
- [ ] Week 2 — A Jenkinsfile that builds, tests, analyses and publishes automatically
- [ ] Week 3 — The same pipeline three ways, plus a written comparison
- [ ] Week 4 — Infrastructure created and destroyed with two commands
- [ ] Week 5 — A server never configured by hand, and a dashboard that reports breakage
- [ ] Week 6 — A production-shaped private network, deployed into by a pipeline
- [ ] Week 7 — The whole stack from one `docker compose up`, images published
- [ ] Week 8 — The app on Kubernetes from a Helm chart, cluster built by Terraform
- [ ] Week 9 — Full GitOps capstone: commit to Git reaches a live cluster on its own

---

## Part 8 — Keeping admin near zero

- **Do not add new columns.** Everything needed is already there.
- **Do not tick tasks in advance.** A tracker that lies is worse than no tracker.
- **The only fields Yacoub edits are:** `Status`, `GitHub Evidence`, `LinkedIn URL`, `Notes`.
  Everything else is reference data set once at import.
- **If a day is missed,** do not reschedule 360 rows. Leave the dates alone and let the
  `Not Started` rows in the past stand as an honest record. The Tuesday/Thursday afternoons
  and Sunday catch-up slots exist to absorb slippage without redesigning the plan.
- **Weekly review, five minutes, every Sunday:** open THIS WEEK, look at anything still
  `Not Started`, and decide honestly whether to catch up or let it go. Then move on.

---

## Troubleshooting the setup

| Problem | Cause | Fix |
|---|---|---|
| Dates show as plain text, calendar view is empty | `Date` is still type Text | Change the property type to Date (Part 2) |
| Board view has one giant column | `Status` is still Text, not Select | Change to Select, then group by it again |
| TODAY view is empty | Filter set to "Is → Exact date" instead of "Is → Today" | Re-set the filter to the relative option **Today** |
| Import created 360 separate pages, not a database | You used "Merge with CSV" on a page instead of Import | Delete and redo Part 1 on a blank page |
| Special characters look wrong (â€") | Editor opened the CSV and re-saved it as ANSI | Re-import the original file; it is UTF-8 with BOM |
