# Mini Restaurant Order Manager

A small web application for creating and managing restaurant orders. It is the group's practical project for Homework 2: AI-Assisted Development and Testing.

## Features

- Create an order with one or more menu items.
- Validate customer names, item names, quantities, and prices.
- Calculate the order total automatically.
- List all orders and retrieve an order by ID.
- Change order status (`pending`, `preparing`, `ready`, `delivered`, `cancelled`).
- Reject invalid input and invalid status transitions.
- Prevent status changes after an order becomes `delivered` or `cancelled`.

## Technology Stack

- Python 3.10+
- Flask
- pytest

## Run Locally on Windows

Open CMD in the project folder and execute:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

Open your browser at:

http://127.0.0.1:5000

## Run Automated Tests

On Windows, with the virtual environment activated:

```cmd
python -m pytest -v
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/orders` | Create a new order |
| GET | `/api/orders` | List all orders |
| GET | `/api/orders/<id>` | Retrieve an order |
| PATCH | `/api/orders/<id>/status` | Update order status |

## API Example

Create an order:

```json
{
  "customer": "Amira",
  "items": [
    {
      "name": "Pizza",
      "quantity": 2,
      "unit_price": 12.5
    }
  ]
}
```

Update order status:

```json
{
  "status": "preparing"
}
```

## Testing Results

### Automated Testing

- Total automated tests executed: 18
- Tests passed: 18
- Tests failed: 0
- Execution time: 0.24 seconds
- Result: All automated tests passed successfully.

### Manual Testing

The following scenarios were tested manually through the web interface:

- Creating an order and checking its registration.
- Updating order statuses.
- Preventing status changes after an order becomes `delivered` or `cancelled`.

All the manual scenarios listed above were successful.

## Important Limitations

This is an educational prototype. Data is kept in memory and is lost when the server restarts. It has no authentication, database, payment integration, or production security hardening.

## Team Members

- Developer 1: [yassine waili]
- Developer 2: [yassine selmi]
- Tester 1: [nadhem abaab]
