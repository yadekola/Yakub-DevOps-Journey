import os
import tempfile

import pytest

# Point the app at a throwaway SQLite file BEFORE importing it, and make sure no Redis
# is configured - tests must not need any running service.
_tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
os.environ["DATABASE_URL"] = f"sqlite:///{_tmp.name}"
os.environ["REDIS_URL"] = ""
os.environ["APP_ENV"] = "test"

from fastapi.testclient import TestClient  # noqa: E402

from app.db import Base, engine  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def an_item(client):
    r = client.post("/api/items", json={
        "sku": "TST-001", "name": "Test Widget", "category": "test",
        "quantity": 10, "reorder_level": 3,
    })
    assert r.status_code == 201
    return r.json()
