
def valid_payload():
    return {
        "customer": "Amira",
        "items": [
            {"name": "Pizza", "quantity": 2, "unit_price": 12.5},
            {"name": "Juice", "quantity": 1, "unit_price": 3}
        ]
    }


def test_create_order_and_calculate_total(client):
    response = client.post("/api/orders", json=valid_payload())
    assert response.status_code == 201
    data = response.get_json()
    assert data["id"] == 1
    assert data["total"] == 28.0
    assert data["status"] == "pending"


def test_list_orders(client):
    client.post("/api/orders", json=valid_payload())
    response = client.get("/api/orders")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_list_multiple_orders(client):
    client.post("/api/orders", json=valid_payload())
    client.post("/api/orders", json=valid_payload())

    response = client.get("/api/orders")

    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_get_unknown_order(client):
    response = client.get("/api/orders/999")
    assert response.status_code == 404


def test_get_existing_order(client):
    created = client.post("/api/orders", json=valid_payload()).get_json()

    response = client.get(f"/api/orders/{created['id']}")

    assert response.status_code == 200
    assert response.get_json()["customer"] == "Amira"


def test_reject_blank_customer(client):
    payload = valid_payload()
    payload["customer"] = "   "

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_reject_empty_items(client):
    payload = valid_payload()
    payload["items"] = []

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_reject_zero_quantity(client):
    payload = valid_payload()
    payload["items"][0]["quantity"] = 0

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_reject_negative_quantity(client):
    payload = valid_payload()
    payload["items"][0]["quantity"] = -1

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_reject_negative_price(client):
    payload = valid_payload()
    payload["items"][0]["unit_price"] = -1

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_accept_zero_price(client):
    payload = valid_payload()
    payload["items"][0]["unit_price"] = 0

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 201
    assert response.get_json()["items"][0]["unit_price"] == 0.0


def test_reject_boolean_quantity(client):
    payload = valid_payload()
    payload["items"][0]["quantity"] = True

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_reject_boolean_price(client):
    payload = valid_payload()
    payload["items"][0]["unit_price"] = True

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_reject_invalid_item_name(client):
    payload = valid_payload()
    payload["items"][0]["name"] = "   "

    response = client.post("/api/orders", json=payload)

    assert response.status_code == 400


def test_update_status(client):
    created = client.post("/api/orders", json=valid_payload()).get_json()

    response = client.patch(
        f"/api/orders/{created['id']}/status",
        json={"status": "preparing"}
    )

    assert response.status_code == 200
    assert response.get_json()["status"] == "preparing"


def test_reject_invalid_status(client):
    created = client.post("/api/orders", json=valid_payload()).get_json()

    response = client.patch(
        f"/api/orders/{created['id']}/status",
        json={"status": "flying"}
    )

    assert response.status_code == 400


def test_terminal_delivered_cannot_be_changed(client):
    created = client.post("/api/orders", json=valid_payload()).get_json()
    order_id = created["id"]

    client.patch(
        f"/api/orders/{order_id}/status",
        json={"status": "delivered"}
    )

    response = client.patch(
        f"/api/orders/{order_id}/status",
        json={"status": "preparing"}
    )

    assert response.status_code == 400


def test_terminal_cancelled_cannot_be_changed(client):
    created = client.post("/api/orders", json=valid_payload()).get_json()
    order_id = created["id"]

    client.patch(
        f"/api/orders/{order_id}/status",
        json={"status": "cancelled"}
    )

    response = client.patch(
        f"/api/orders/{order_id}/status",
        json={"status": "preparing"}
    )

    assert response.status_code == 400
