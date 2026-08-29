def test_create_and_fetch_item(client):
    r = client.post("/api/items", json={"sku": "A-1", "name": "Thing", "quantity": 7})
    assert r.status_code == 201
    body = r.json()
    assert body["sku"] == "A-1"
    assert body["quantity"] == 7

    r2 = client.get(f"/api/items/{body['id']}")
    assert r2.status_code == 200
    assert r2.json()["name"] == "Thing"


def test_duplicate_sku_returns_409_not_500(client, an_item):
    r = client.post("/api/items", json={"sku": "TST-001", "name": "Clash"})
    assert r.status_code == 409
    assert "already exists" in r.json()["detail"]


def test_missing_item_returns_404(client):
    assert client.get("/api/items/99999").status_code == 404


def test_negative_quantity_is_rejected_by_validation(client):
    r = client.post("/api/items", json={"sku": "B-1", "name": "Bad", "quantity": -5})
    assert r.status_code == 422


def test_low_stock_endpoint_uses_reorder_level(client):
    client.post("/api/items", json={"sku": "LOW-1", "name": "Low", "quantity": 2, "reorder_level": 5})
    client.post("/api/items", json={"sku": "OK-1", "name": "Fine", "quantity": 50, "reorder_level": 5})
    skus = [i["sku"] for i in client.get("/api/items/low-stock").json()]
    assert "LOW-1" in skus
    assert "OK-1" not in skus


def test_search_and_category_filters(client, an_item):
    client.post("/api/items", json={"sku": "Z-9", "name": "Zebra", "category": "animals"})
    assert len(client.get("/api/items?category=animals").json()) == 1
    assert len(client.get("/api/items?search=zeb").json()) == 1
