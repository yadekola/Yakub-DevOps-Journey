# Extension exercises

Deploying someone else's application teaches you deployment. **Extending it teaches you
the codebase** — and the difference shows immediately in an interview, because you can
only answer "why did you build it that way?" about code you have actually changed.

Do at least four of these before the capstone. Each one is a real commit, a real test, and
a real LinkedIn post.

Ordered easy → hard. Each says what to change and how to know you succeeded.

---

## 1. Add a supplier field to items  *(easy, ~30 min)*

**Change:** add `supplier: str` to the `Item` model, `ItemCreate` and `ItemOut`. Show it in
the frontend table.

**Verify:** create an item with a supplier, see it in `GET /api/items` and in the browser.

**What you'll learn:** why `Base.metadata.create_all()` does NOT add a column to an
existing table. Your new field will silently fail against an existing database. That
frustration is the entire motivation for exercise 9.

---

## 2. Add a `GET /api/items/{id}/history` endpoint  *(easy)*

**Change:** return that item's movements, newest first, with a `?limit=` parameter.

**Verify:** write a test that creates three movements and asserts the order.

---

## 3. Sort and paginate the item list  *(easy)*

**Change:** add `?sort=name|quantity|updated_at` and `&order=asc|desc` to `GET /api/items`.

**Verify:** a test per sort field. Reject an invalid sort value with 422, not 500.

**Watch out:** never interpolate the sort column into raw SQL. Map allowed values to model
attributes explicitly — that's the difference between a feature and a SQL injection.

---

## 4. Add a business alert metric  *(easy, high interview value)*

**Change:** add `stockpulse_stock_outs_total` — a counter incremented every time an `out`
movement is rejected for insufficient stock.

**Verify:** trigger a few rejections, see the counter climb at `/metrics`.

**Then:** build a Grafana panel and an alert on it. "I alert when staff try to sell stock
we don't have" is a far better story than "I alert on 80% CPU".

---

## 5. Bulk import from CSV  *(medium)*

**Change:** `POST /api/items/bulk` accepting a CSV upload. Report per-row successes and
failures rather than failing the whole batch on one bad row.

**Verify:** upload a file where row 3 has a duplicate SKU. Rows 1, 2, 4 should succeed and
the response should say exactly which row failed and why.

**What you'll learn:** partial-failure design — a genuinely hard problem that comes up
constantly in real systems.

---

## 6. Rate-limit the write endpoints  *(medium)*

**Change:** use Redis to limit POST requests to 30/minute per IP. Return 429 with a
`Retry-After` header.

**Verify:** a loop of 40 requests; the last ten get 429.

**The subtle part:** Redis is optional in this app. Decide — does rate limiting fail open
(allow everything if Redis is down) or fail closed (reject everything)? There is a right
answer for this app. Write your reasoning in the commit message.

---

## 7. Add API-key authentication  *(medium)*

**Change:** require an `X-API-Key` header on all write endpoints. Read endpoints stay open.
Key comes from an environment variable.

**Verify:** writes without the header return 401; reads still work.

**Then:** wire the key through Docker Compose `.env`, GitHub Secrets, and a Kubernetes
Secret. This one exercise touches every secret-management mechanism in the course.

---

## 8. Structured request logging with correlation IDs  *(medium)*

**Change:** generate a UUID per request, include it in every log line, return it as an
`X-Request-ID` header. Accept an incoming one if present.

**Verify:** make a request, find every log line for it by that ID alone.

**Why:** when you have five API pods and a user reports an error at 14:32, this is how you
find their specific request.

---

## 9. Replace `create_all()` with Alembic migrations  *(hard, most valuable)*

**Change:** add Alembic, generate an initial migration, remove `Base.metadata.create_all()`
from the lifespan handler. Run migrations as a separate step.

**Verify:** add exercise 1's supplier column *as a migration*, apply it to a database that
already has data, and confirm the existing rows survive.

**Then:** run migrations as a Kubernetes **init container** or a **Job**, not on app
startup. Ask yourself what happens when three API pods start simultaneously and all try to
migrate the same database at once. That question is a senior-level interview topic and you
will have a real answer.

---

## 10. Graceful shutdown  *(hard)*

**Change:** handle SIGTERM — stop accepting new requests, finish in-flight ones, close the
DB pool, then exit. Add a `preStop` hook and `terminationGracePeriodSeconds` in Kubernetes.

**Verify:** run a load loop, delete the pod mid-flight, and show zero failed requests.

**Why it matters:** this is the difference between a rolling deploy that drops user
requests and one that doesn't. Demonstrating zero-downtime deploys with evidence puts you
ahead of most junior candidates.

---

## 11. Read replica support  *(hard)*

**Change:** route reads to a replica connection and writes to the primary.

**Verify:** two Postgres containers with streaming replication; show reads served by the
replica.

**Then explain:** replication lag. A user adds an item and immediately doesn't see it in
the list. What do you do about it?

---

## 12. Multi-architecture image build  *(hard)*

**Change:** build the API image for both `linux/amd64` and `linux/arm64` with Buildx in
GitHub Actions.

**Verify:** `docker manifest inspect` shows both architectures.

---

## How to work an exercise

```
1. Write the test FIRST. It should fail.
2. Make the change until the test passes.
3. Run the whole suite - make sure you broke nothing.
4. Update the README if the API changed.
5. Commit with a message explaining WHY, not just what.
6. LinkedIn post: what you built, what broke, what you learned.
```

If you cannot explain a change you made a week later, you did not do the exercise — you
copied a solution. Redo it.
