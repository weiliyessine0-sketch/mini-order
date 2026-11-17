
from flask import Flask, jsonify, request, render_template_string
from app.order_service import OrderService, ValidationError

PAGE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mini Restaurant Order Manager</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f4;
            margin: 0;
            color: #1d2a22;
        }

        header {
            background: #173d2b;
            color: white;
            padding: 24px;
            text-align: center;
        }

        main {
            max-width: 900px;
            margin: 24px auto;
            padding: 0 16px;
        }

        .panel {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 18px;
            box-shadow: 0 2px 12px #0001;
        }

        input, button, select {
            padding: 10px;
            margin: 5px;
            border: 1px solid #ccd5ce;
            border-radius: 7px;
        }

        button {
            background: #24613f;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #173d2b;
        }

        .order {
            border-bottom: 1px solid #e4e9e5;
            padding: 12px 0;
        }

        small {
            color: #65736a;
        }

        #message {
            font-weight: bold;
        }

        .terminal {
            color: #65736a;
            font-style: italic;
        }
    </style>
</head>

<body>

<header>
    <h1>Mini Restaurant Order Manager</h1>
    <p>Educational order tracking prototype</p>
</header>

<main>

    <section class="panel">
        <h2>Create an order</h2>

        <form id="orderForm">
            <input
                id="customer"
                placeholder="Customer name"
                required
            >

            <div id="itemRows">
                <div class="item-row">
                    <input class="item-name" placeholder="Item name" required>
                    <input class="item-quantity" type="number" min="1" step="1" value="1" aria-label="Quantity" required>
                    <input class="item-price" type="number" min="0" step="0.01" placeholder="Unit price" aria-label="Unit price" required>
                    <button type="button" class="remove-item" aria-label="Remove item" hidden>Remove</button>
                </div>
            </div>
            <button id="addItemButton" type="button">Add another item</button>

            <button type="submit">Create order</button>
        </form>

        <p id="message" role="status"></p>
    </section>

    <section class="panel">
        <h2>Orders</h2>

        <button id="refreshButton" type="button">
            Refresh
        </button>

        <div id="orders">Loading...</div>
    </section>

</main>

<script>
const orderForm = document.getElementById('orderForm');
const customerInput = document.getElementById('customer');
const itemRows = document.getElementById('itemRows');
const addItemButton = document.getElementById('addItemButton');
const messageElement = document.getElementById('message');
const ordersElement = document.getElementById('orders');
const refreshButton = document.getElementById('refreshButton');

function updateRemoveButtons() {
    const rows = itemRows.querySelectorAll('.item-row');
    rows.forEach(row => {
        row.querySelector('.remove-item').hidden = rows.length === 1;
    });
}

addItemButton.addEventListener('click', () => {
    const row = document.createElement('div');
    row.className = 'item-row';
    row.innerHTML = `
        <input class="item-name" placeholder="Item name" required>
        <input class="item-quantity" type="number" min="1" step="1" value="1" aria-label="Quantity" required>
        <input class="item-price" type="number" min="0" step="0.01" placeholder="Unit price" aria-label="Unit price" required>
        <button type="button" class="remove-item" aria-label="Remove item">Remove</button>
    `;
    itemRows.appendChild(row);
    updateRemoveButtons();
});

itemRows.addEventListener('click', event => {
    if (event.target.classList.contains('remove-item')) {
        event.target.closest('.item-row').remove();
        updateRemoveButtons();
    }
});

const nextStatuses = {
    pending: ['preparing', 'cancelled'],
    preparing: ['ready', 'cancelled'],
    ready: ['delivered', 'cancelled'],
    delivered: [],
    cancelled: []
};

function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
    })[character]);
}

async function loadOrders() {
    ordersElement.textContent = 'Loading...';

    try {
        const response = await fetch('/api/orders');
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Unable to load orders.');
        }

        if (!Array.isArray(data) || data.length === 0) {
            ordersElement.textContent = 'No orders yet.';
            return;
        }

        ordersElement.innerHTML = data.map(order => {
            const isTerminal =
                order.status === 'delivered' ||
                order.status === 'cancelled';

            const items = order.items.map(product =>
                `${escapeHtml(product.name)} × ${product.quantity}`
            ).join(', ');

            const options = [order.status, ...nextStatuses[order.status]].map(status => `
                <option value="${status}"
                    ${status === order.status ? 'selected' : ''}>
                    ${status}
                </option>
            `).join('');

            return `
                <div class="order">
                    <b>
                        #${order.id} — ${escapeHtml(order.customer)}
                    </b>

                    <br>
                    ${items}

                    <br>
                    <b>Total: ${Number(order.total).toFixed(2)}</b>
                    | Status: ${escapeHtml(order.status)}

                    <br>
                    <small>Update status:</small>

                    ${
                        isTerminal
                        ? '<span class="terminal">Final status — cannot be changed.</span>'
                        : `
                            <select
                                onchange="changeStatus(${order.id}, this.value)">
                                ${options}
                            </select>
                        `
                    }
                </div>
            `;
        }).join('');

    } catch (error) {
        ordersElement.textContent =
            'Error loading orders: ' + error.message;
    }
}

orderForm.addEventListener('submit', async event => {
    event.preventDefault();

    messageElement.textContent = 'Creating order...';

    const payload = {
        customer: customerInput.value,
        items: Array.from(itemRows.querySelectorAll('.item-row')).map(row => ({
            name: row.querySelector('.item-name').value,
            quantity: Number(row.querySelector('.item-quantity').value),
            unit_price: Number(row.querySelector('.item-price').value)
        }))
    };

    try {
        const response = await fetch('/api/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            messageElement.textContent =
                data.error || 'Unable to create order.';
            return;
        }

        messageElement.textContent =
            `Order #${data.id} created. Total: ${Number(data.total).toFixed(2)}`;

        orderForm.reset();
        itemRows.querySelectorAll('.item-row:not(:first-child)').forEach(row => row.remove());
        itemRows.querySelector('.item-quantity').value = 1;
        updateRemoveButtons();

        await loadOrders();

    } catch (error) {
        messageElement.textContent =
            'Connection error: ' + error.message;
    }
});

async function changeStatus(id, status) {
    try {
        const response = await fetch(
            `/api/orders/${id}/status`,
            {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || 'Unable to update order status.');
        }

        await loadOrders();

    } catch (error) {
        alert('Connection error: ' + error.message);
        await loadOrders();
    }
}

refreshButton.addEventListener('click', loadOrders);

loadOrders();
</script>

</body>
</html>
'''


def create_app(service=None):
    app = Flask(__name__)
    app.config["service"] = service or OrderService()

    @app.get("/")
    def home():
        return render_template_string(PAGE)

    @app.post("/api/orders")
    def create_order():
        try:
            order = app.config["service"].create_order(
                request.get_json(silent=True)
            )

            return jsonify(order.to_dict()), 201

        except ValidationError as exc:
            return jsonify({"error": str(exc)}), 400

    @app.get("/api/orders")
    def list_orders():
        return jsonify(app.config["service"].list_orders())

    @app.get("/api/orders/<int:order_id>")
    def get_order(order_id):
        order = app.config["service"].get_order(order_id)

        if order is None:
            return jsonify({"error": "Order not found."}), 404

        return jsonify(order.to_dict())

    @app.patch("/api/orders/<int:order_id>/status")
    def update_status(order_id):
        body = request.get_json(silent=True)

        if not isinstance(body, dict):
            return jsonify({
                "error": "Request body must be a JSON object."
            }), 400

        try:
            order = app.config["service"].update_status(
                order_id,
                body.get("status")
            )

            if order is None:
                return jsonify({"error": "Order not found."}), 404

            return jsonify(order.to_dict())

        except ValidationError as exc:
            return jsonify({"error": str(exc)}), 400

    return app
