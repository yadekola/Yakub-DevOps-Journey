# Configuration and running without containerized Node.js

## Environment variables

| Variable | Example/default | Used by | Purpose |
|---|---|---|---|
| POSTGRES_DB | inventory | db, api, migrate | Database name |
| POSTGRES_USER | inventory | db, api, migrate | Database username |
| POSTGRES_PASSWORD | local-inventory-change-me | db, api, migrate | Local example password |
| WEB_PORT | 5173 |  | Host-side frontend port |
| API_PORT | 3000 |  | Host-side API port |
| NODE_ENV | production | Node.js | Runtime mode |
| DB_HOST | db in Compose | Node.js | Database hostname |
| DB_PORT | 5432 in Compose | Node.js | Database port |
| PORT | 3000 in Compose | Node.js | Internal HTTP listening port |

The connection pool has at most 10 connections, a 5-second connection timeout, a 30-second idle timeout and a 5-second statement timeout. These settings live in `backend/src/config.js`. 

Do not commit `.env` with real credentials. `.env.example` contains only demonstration values. Changing POSTGRES_PASSWORD after the database volume has initialized does not change the database role password. See troubleshooting before editing existing credentials.

## Run React and Express directly on your computer

Requirements: Node.js 24, npm and PostgreSQL 17.

**Terminal 1, backend, PowerShell:**

```powershell
cd backend
Copy-Item .env.local.example .env
npm ci
node --env-file=.env src/migrate.js
node --env-file=.env src/seed.js
node --env-file=.env --watch src/server.js

#command to run backend server
node src/server.js
```

On Linux/macOS use `cp .env.local.example .env` instead of Copy-Item. Keep backend `.env` database credentials consistent with the root `.env`.

**Terminal 2, frontend, from the project root:**

```bash
cd frontend
npm ci
npm run dev
```

Open **http://localhost:5173**. Vite proxies `/api` to localhost:3000. The browser code uses relative `/api` paths, so no CORS configuration is needed. Port 5173 is used for host development only; the full Docker stack uses localhost:8081.

If using an independently installed PostgreSQL server, create the inventory database and login first, change backend `.env` DB_HOST/DB_PORT to match that server, and omit the Docker database commands. The default local-db override uses port 5433, not 5432, on your computer.



