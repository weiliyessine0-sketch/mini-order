
from dataclasses import dataclass, asdict
from typing import Any

VALID_STATUSES = {"pending", "preparing", "ready", "delivered", "cancelled"}
ALLOWED_STATUS_TRANSITIONS = {
    "pending": {"preparing", "cancelled"},
    "preparing": {"ready", "cancelled"},
    "ready": {"delivered", "cancelled"},
    "delivered": set(),
    "cancelled": set(),
}


class ValidationError(ValueError):
    pass


@dataclass
class Order:
    id: int
    customer: str
    items: list[dict[str, Any]]
    total: float
    status: str = "pending"

    def to_dict(self):
        return asdict(self)


class OrderService:
    def __init__(self):
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def create_order(self, payload):
        if not isinstance(payload, dict):
            raise ValidationError("Request body must be a JSON object.")

        customer = payload.get("customer")
        if not isinstance(customer, str) or not customer.strip():
            raise ValidationError("Customer name is required.")

        items = payload.get("items")
        if not isinstance(items, list) or not items:
            raise ValidationError("At least one item is required.")

        clean_items = []
        total = 0.0

        for index, item in enumerate(items):
            if not isinstance(item, dict):
                raise ValidationError(f"Item {index + 1} must be an object.")

            name = item.get("name")
            quantity = item.get("quantity")
            price = item.get("unit_price")

            if not isinstance(name, str) or not name.strip():
                raise ValidationError(f"Item {index + 1}: name is required.")

            if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
                raise ValidationError(
                    f"Item {index + 1}: quantity must be a positive integer."
                )

            if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
                raise ValidationError(
                    f"Item {index + 1}: unit_price must be a non-negative number."
                )

            line_total = quantity * float(price)
            total += line_total

            clean_items.append({
                "name": name.strip(),
                "quantity": quantity,
                "unit_price": round(float(price), 2),
                "line_total": round(line_total, 2),
            })

        order = Order(
            id=self._next_id,
            customer=customer.strip(),
            items=clean_items,
            total=round(total + 1e-10, 2),
        )

        self._orders[order.id] = order
        self._next_id += 1

        return order

    def list_orders(self):
        return [order.to_dict() for order in self._orders.values()]

    def get_order(self, order_id):
        return self._orders.get(order_id)

    def update_status(self, order_id, status):
        order = self._orders.get(order_id)

        if order is None:
            return None

        if not isinstance(status, str) or status not in VALID_STATUSES:
            raise ValidationError(
                f"Status must be one of: {', '.join(sorted(VALID_STATUSES))}."
            )

        if status == order.status:
            return order

        if status not in ALLOWED_STATUS_TRANSITIONS[order.status]:
            raise ValidationError(
                f"Order cannot move from '{order.status}' to '{status}'."
            )

        order.status = status
        return order
