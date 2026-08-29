def test_stock_in_increases_quantity(client, an_item):
    r = client.post("/api/movements", json={"sku": "TST-001", "kind": "in", "quantity": 5})
    assert r.status_code == 201
    assert client.get(f"/api/items/{an_item['id']}").json()["quantity"] == 15


def test_stock_out_decreases_quantity(client, an_item):
    client.post("/api/movements", json={"sku": "TST-001", "kind": "out", "quantity": 4})
    assert client.get(f"/api/items/{an_item['id']}").json()["quantity"] == 6


def test_stock_cannot_go_negative(client, an_item):
    r = client.post("/api/movements", json={"sku": "TST-001", "kind": "out", "quantity": 999})
    assert r.status_code == 409
    assert "insufficient stock" in r.json()["detail"]


def test_rejected_movement_writes_nothing(client, an_item):
    """The transaction rule: quantity unchanged AND no movement row created."""
    client.post("/api/movements", json={"sku": "TST-001", "kind": "out", "quantity": 999})
    assert client.get(f"/api/items/{an_item['id']}").json()["quantity"] == 10
    assert client.get("/api/movements?sku=TST-001").json() == []


def test_adjust_sets_absolute_quantity(client, an_item):
    client.post("/api/movements", json={"sku": "TST-001", "kind": "adjust", "quantity": 3,
                                        "note": "stock take"})
    assert client.get(f"/api/items/{an_item['id']}").json()["quantity"] == 3


def test_movement_against_unknown_sku_is_404(client):
    r = client.post("/api/movements", json={"sku": "NOPE", "kind": "in", "quantity": 1})
    assert r.status_code == 404


def test_movement_creates_audit_trail(client, an_item):
    client.post("/api/movements", json={"sku": "TST-001", "kind": "in", "quantity": 2,
                                        "note": "delivery"})
    rows = client.get("/api/movements?sku=TST-001").json()
    assert len(rows) == 1
    assert rows[0]["note"] == "delivery"
