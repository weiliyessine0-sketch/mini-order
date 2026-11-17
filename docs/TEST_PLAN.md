# Test Plan — Mini Restaurant Order Manager

## 1. Objective

The objective of this test plan is to verify that the Mini Restaurant Order Manager application works correctly and meets the acceptance criteria defined in `SPEC.md`.

The testing process focuses on order creation, input validation, total calculation, order retrieval, order listing, and order status management.

## 2. Scope

### Included
- Creating new restaurant orders.
- Validating customer information and order items.
- Calculating order totals.
- Listing all orders.
- Retrieving a specific order.
- Updating order statuses.
- Preventing status changes after an order reaches a terminal status.
- Testing the main browser workflow and API endpoints.

### Excluded
- User authentication and authorization.
- Database persistence.
- Online payments.
- Load and performance testing.
- External service integrations.

## 3. Test Approach

The project uses three testing approaches:

### 3.1 Functional Testing
- Create an order with valid information.
- Display the list of registered orders.
- Retrieve an existing order.
- Update an order status.
- Verify that order totals are calculated correctly.

### 3.2 Boundary Testing
The following boundary scenarios are included in the planned test cases:
- Minimum valid quantity (1).
- Zero price.
- Decimal prices.
- Empty item list.
- Whitespace-only customer name.

### 3.3 Negative Testing
The application is checked against invalid inputs and operations, including:
- Missing or invalid customer information.
- Missing or invalid item fields.
- Negative prices.
- Zero or invalid quantities.
- Invalid order statuses.
- Unknown order IDs.
- Attempts to change an order after it reaches a terminal status.

### 3.4 Automated Testing
Automated tests are implemented using:
- Python.
- pytest.
- Flask test client.

The automated tests verify the main order service and API behavior.

### 3.5 Manual Testing
Manual testing is performed through the browser to verify:
- Opening the application homepage.
- Creating an order.
- Checking that the order appears in the list.
- Changing order statuses.
- Verifying that delivered and cancelled orders cannot be changed again.
- Verifying the terminal-status message in the interface.

## 4. Environment and Resources

- Operating System: Windows.
- Programming Language: Python 3.10+.
- Web Framework: Flask.
- Testing Framework: pytest.
- Browser: Any modern web browser.
- Dependencies: Listed in `requirements.txt`.
- Project source code: Project repository.

## 5. Roles and Responsibilities

- **Tester 1:** Prepare test cases and test data.
- **Tester 2:** Execute manual and automated tests and record results.
- **Developer 1:** Implement application features and fix identified defects.
- **Developer 2:** Review AI-generated code, integrate changes, and perform regression testing.

All team members are responsible for reviewing the results and understanding the code.

## 6. Test Schedule

The following schedule is a suggested project testing plan.

| Activity | Responsible | Estimated Duration |
|---|---|---:|
| Review specification and identify risks | Testers | 1 hour |
| Prepare test cases and test data | Testers | 2 hours |
| Execute automated tests | Tester 2 | 1 hour |
| Perform manual browser testing | Both testers | 1 hour |
| Report defects and retest fixes | Whole team | 2 hours |
| Regression testing and final evidence | Whole team | 1 hour |

## 7. Entry Criteria

Testing can begin when:
- The project specification has been reviewed.
- The application can start successfully.
- Python and the required dependencies are installed.
- The test environment is ready.

## 8. Test Execution Results

### 8.1 Automated Testing

- Testing framework: pytest.
- Execution command: `python -m pytest -v`.
- Total automated tests executed: 18.
- Passed: 18.
- Failed: 0.
- Execution time: 0.24 seconds.

**Result:** All 18 automated tests passed successfully.

### 8.2 Manual Testing

The following manual tests were executed through the browser:

| Test ID | Description | Result |
|---|---|---|
| MT-01 | Create a new order | PASS |
| MT-02 | Verify that the order appears in the list | PASS |
| MT-03 | Change order status to delivered | PASS |
| MT-04 | Prevent changes after delivered | PASS |
| MT-05 | Change order status to cancelled | PASS |
| MT-06 | Prevent changes after cancelled | PASS |
| MT-07 | Verify terminal-status interface message | PASS |

**Result:** All seven recorded manual tests passed.

Note: The results above represent the tests actually executed. Other planned scenarios must be executed before they can be reported as passed.

## 9. Exit Criteria

Testing is considered complete when:
- Planned test cases have been executed or their remaining status is documented.
- Critical defects have been fixed or clearly documented.
- Automated regression tests pass.
- Manual test results are recorded.
- Test evidence and known limitations are included in the final report.

## 10. Risks

The main project risks include:
- Differences between Python and dependency versions.
- Incomplete or unclear requirements.
- Invalid user input.
- Unexpected application behavior.
- Loss of orders when the application restarts because data is stored in memory.

## 11. Known Limitations

- Orders are stored in memory and are lost when the application restarts.
- The application does not include authentication.
- The application does not support online payments.
- Not every planned boundary and negative test scenario has been confirmed as executed.
- The application is intended as a small academic project and not as a complete production restaurant management system.

## 12. Conclusion

The testing results show that the main order management features work correctly.

All 18 automated tests passed, and all seven recorded manual tests passed.

Further testing of the remaining planned scenarios is recommended to improve test coverage and confidence in the application.