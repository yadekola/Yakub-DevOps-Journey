# API reference

Base address through frontend: `http://localhost:5173`.
Direct API address: `http://localhost:3000`.

All paths below include `/api`. No authentication is configured. Routes are documented without trailing slashes; Express also accepts a trailing slash. Write requests must send `Content-Type: application/json`. Responses use JSON except successful deletion, which returns an empty body.

## Endpoints

| Method | Path | Purpose | Successful response |
|---|---|---|---|
| GET | /api | API name, version and currency | 200 |
| GET | /api/openapi.json | OpenAPI specification | 200 |
| GET | /api/health/live | Confirm Node process is serving requests | 200 |
| GET | /api/health/ready | Confirm database connection and products table | 200 |
| GET | /api/products | List, search, filter and paginate products | 200 |
| POST | /api/products | Create a product | 201 |
| GET | /api/products/{id} | Read one product | 200 |
| PUT | /api/products/{id} | Replace all editable fields | 200 |
| PATCH | /api/products/{id} | Change supplied fields only | 200 |
| DELETE | /api/products/{id} | Delete a product | 204, no body |

## Product fields

| Field | Type | Validation |
|---|---|---|
| id | integer | Generated, read-only |
| sku | string | 1 to 40 characters; letters, digits, underscore or hyphen; starts with a letter/digit; converted to uppercase; unique |
| name | string | Nonblank, at most 160 characters |
| category | string | Nonblank, at most 80 characters |
| price_minor | integer | 0 to 1,000,000,000 kobo, representing at most NGN 10,000,000.00 |
| quantity | integer | 0 to 1,000,000,000 |
| created_at | datetime | Generated UTC timestamp, read-only |
| updated_at | datetime | Updated by API writes, read-only |

POST and PUT require all five editable fields. PATCH requires at least one editable field. Unknown and read-only fields in input are rejected. Numbers must be JSON numbers, not strings. Blank strings and negative quantities are rejected. Text is trimmed before storage.

Create/replace example:

```json
{
  "sku": "KB-001",
  "name": "Wireless keyboard",
  "category": "Accessories",
  "price_minor": 1850000,
  "quantity": 24
}
```

Example create response (ID and timestamps are illustrative):

```json
{
  "data": {
    "id": 1,
    "sku": "KB-001",
    "name": "Wireless keyboard",
    "category": "Accessories",
    "price_minor": 1850000,
    "quantity": 24,
    "created_at": "2026-10-10T12:00:00.000Z",
    "updated_at": "2026-10-10T12:00:00.000Z"
  }
}
```

POST also includes a `Location` header such as `/api/products/1`.

PATCH body example:

```json
{"quantity": 30}
```

## List parameters

| Query | Default | Meaning |
|---|---|---|
| page | 1 | Page number, 1 to 1,000,000 |
| limit | 10 | Results per page, 1 to 100 |
| search | Empty | Case-insensitive matching of name or SKU |
| category | Empty | Exact, case-sensitive category match |

Example: `/api/products?search=keyboard&category=Accessories&page=1&limit=10`.

Search uses SQL ILIKE patterns. `%` matches any sequence and `_` matches one character. The values remain parameterized, so these are search wildcards, not executable SQL. Search and category parameters accept up to 160 characters. Repeated parameters are rejected. Unrecognized query parameter names are ignored.

The list is ordered by descending ID. Example response:

```json
{
  "data": [],
  "pagination": {"page": 1, "limit": 10, "total": 0, "total_pages": 0}
}
```

When products exist, `data` contains product objects. A page beyond the last page returns an empty array with status 200. List counts and rows use two queries and can briefly differ if another client writes concurrently.

## Errors

| Status | Code | Meaning |
|---|---|---|
| 400 | VALIDATION_ERROR | Invalid or missing product fields |
| 400 | INVALID_JSON | Malformed JSON body |
| 400 | INVALID_QUERY | Invalid page, limit or filter value |
| 400 | INVALID_ID | ID is not a positive integer |
| 404 | NOT_FOUND | Product or endpoint not found |
| 409 | SKU_EXISTS | Another product already uses the normalized SKU |
| 413 | BODY_TOO_LARGE | JSON body exceeds 32 KB |
| 415 | UNSUPPORTED_MEDIA_TYPE | Write request does not use application/json |
| 500 | INTERNAL_ERROR | Unexpected request/database failure |
| 503 | NOT_READY | Readiness endpoint cannot query products table |

Example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Check the submitted fields.",
    "details": {"quantity": "Use an integer from 0 to 1000000000."},
    "request_id": "generated-request-identifier"
  }
}
```

Every API response receives an `X-Request-ID` header. Request logs include the same identifier. Unsupported route/method combinations generally fall through to a 404 rather than a dedicated 405. Standard Express behavior also supports HEAD for GET routes and automatic OPTIONS responses.
