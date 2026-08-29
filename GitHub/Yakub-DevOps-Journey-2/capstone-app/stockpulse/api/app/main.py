import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from . import metrics
from .config import settings
from .db import Base, engine
from .routes import health, items, movements, summary

logging.basicConfig(
    level=logging.INFO,
    format='{"ts":"%(asctime)s","level":"%(levelname)s","logger":"%(name)s","msg":"%(message)s"}',
)
log = logging.getLogger("stockpulse")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creates tables if they do not exist. Fine for a learning project.
    # EXTENSION EXERCISE: replace this with Alembic migrations - see docs/EXERCISES.md.
    Base.metadata.create_all(bind=engine)
    log.info("stockpulse started env=%s", settings.app_env)
    yield
    log.info("stockpulse shutting down")


app = FastAPI(
    lifespan=lifespan,
    title="StockPulse API",
    description="Small-shop inventory tracking. Built as a DevOps capstone application.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # fine for a learning project; tighten before production
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def observe(request: Request, call_next):
    started = time.perf_counter()
    response = await call_next(request)
    elapsed_ms = (time.perf_counter() - started) * 1000
    route = request.scope.get("route")
    path = getattr(route, "path", request.url.path)
    if path != "/metrics":                     # do not count the scraper's own requests
        metrics.inc(
            "stockpulse_http_requests_total",
            method=request.method,
            path=path,
            status=response.status_code,
        )
    log.info(
        "%s %s -> %s in %.1fms", request.method, request.url.path, response.status_code, elapsed_ms
    )
    return response


app.include_router(health.router)
app.include_router(items.router)
app.include_router(movements.router)
app.include_router(summary.router)


@app.get("/")
def root():
    return {"service": "stockpulse", "version": app.version, "docs": "/docs"}
