# Software Specification — Mini Restaurant Order Manager

## 1. Project Description

A lightweight web application that allows restaurant staff to record customer orders, calculate totals automatically, view existing orders, and update order preparation status.

The application is developed as a practical project for Homework 2: AI-Assisted Development and Testing.

## 2. Core Features

1. Create an order containing a customer name and one or more items.
2. Validate all submitted data on the server.
3. Calculate the order total as the sum of `quantity × unit_price`.
4. Display all registered orders and retrieve one order by ID.
5. Update an order status using the allowed status workflow.
6. Return clear error messages for invalid requests and unknown orders.

## 3. User Stories

- As a staff member, I want to create an order so that a customer's request is recorded.
- As a staff member, I want the total to be calculated automatically so that I do not calculate it manually.
- As a staff member, I want to view existing orders so that I can follow their progress.
- As a staff member, I want to update the status so that the kitchen and counter know the order state.
- As a staff member, I want invalid data to be rejected so that incorrect orders are not stored.

## 4. Acceptance Criteria

- A valid order returns HTTP 201 and a unique integer ID.
- Customer name must be a non-empty string after trimming whitespace.
- `items` must be a non-empty list.
- Each item must have a non-empty name, an integer quantity greater than zero, and a numeric unit price greater than or equal to zero.
- Boolean values are not accepted as quantities or prices.
- The total is calculated by the server and rounded to two decimal places.
- Unknown order IDs return HTTP 404.
- Only these statuses are accepted: `pending`, `preparing`, `ready`, `delivered`, `cancelled`.
- Allowed transitions are `pending` to `preparing` or `cancelled`, `preparing` to `ready` or `cancelled`, and `ready` to `delivered` or `cancelled`.
- `delivered` and `cancelled` are terminal states; they cannot be changed to another state.
- Invalid requests return HTTP 400 with a readable error message.

## 4.1 Order Status Workflow

The application supports the following order statuses:

- `pending`: The order has been created.
- `preparing`: The kitchen is preparing the order.
- `ready`: The order is ready.
- `delivered`: The order has been delivered.
- `cancelled`: The order has been cancelled.

The `delivered` and `cancelled` statuses are terminal states. Once an order reaches either of these states, its status cannot be changed to another status.

Allowed transitions: `pending` → `preparing` or `cancelled`; `preparing` → `ready` or `cancelled`; `ready` → `delivered` or `cancelled`.

## 5. Technology Stack

- Python 3.10+
- Flask
- pytest
- HTML/CSS

## 6. Out of Scope

The following features are not included in this educational prototype:

- User accounts and authentication.
- Online payment.
- Persistent database storage.
- Inventory management.
- Delivery tracking.
- Multi-branch support.

## 7. Known Technical Limitations

- Orders are stored in memory and are lost when the application restarts.
- The application is intended for educational purposes and is not production-ready.
- Authentication and production security features are not implemented.
