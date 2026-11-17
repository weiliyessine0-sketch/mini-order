# Test Cases — Mini Restaurant Order Manager

## 1. Planned Test Cases

The following test cases define the scenarios selected for testing the application.

| ID | Scenario | Input / Steps | Expected result | Type |
|---|---|---|---|---|
| TC01 | Create valid order | Customer Amira; Pizza qty 2 price 12.50 | 201; total 25.00 | Functional |
| TC02 | Multiple items total | Pizza 2×12.50; Juice 1×3.00 | Total 28.00 | Functional |
| TC03 | List orders | Create one order, GET list | One order returned | Functional |
| TC04 | Unknown order | GET /api/orders/999 | 404 | Negative |
| TC05 | Blank customer | Customer contains spaces only | 400 | Boundary/Negative |
| TC06 | Empty items | items=[] | 400 | Negative |
| TC07 | Quantity zero | quantity=0 | 400 | Boundary/Negative |
| TC08 | Negative quantity | quantity=-1 | 400 | Negative |
| TC09 | Quantity is decimal | quantity=1.5 | 400 | Negative |
| TC10 | Boolean quantity | quantity=true | 400 | Negative |
| TC11 | Zero price | unit_price=0 | Order accepted; line total 0 | Boundary |
| TC12 | Negative price | unit_price=-0.01 | 400 | Negative |
| TC13 | Invalid status | status='flying' | 400 | Negative |
| TC14 | Valid status update | pending → preparing | 200; status preparing | Functional |
| TC15 | Terminal status | delivered → preparing | 400 | Boundary/Negative |
| TC16 | Whitespace item name | name='  ' | 400 | Boundary/Negative |
| TC17 | Non-object item | items=['Pizza'] | 400 | Negative |
| TC18 | Missing JSON body | POST without JSON | 400 | Negative |
| TC19 | Skip workflow | pending → delivered | 400 | Negative |
| TC20 | Follow workflow | pending → preparing → ready → delivered | 200 at each step | Functional |
| TC21 | Cancel active order | pending → cancelled | 200 | Functional |

## 2. Automated Testing Results

Automated tests were executed using pytest and the Flask test client.

**Execution command:**

```cmd
python -m pytest -v
```

| Metric | Result |
|---|---:|
| Automated tests executed | See current pytest output |
| Passed | See current pytest output |
| Failed | See current pytest output |
| Execution time | See current pytest output |

Record the actual result after running the command. Do not assume the planned test cases have all been executed.

Note: The planned test cases above describe the testing scenarios. They should not all be considered individually executed unless they are mapped to an actual automated test or a recorded manual execution.

## 3. Manual Testing Results

**Execution date:** 01/11/2026  
**Testing type:** Manual testing  
**Tester:** Project team

| Test ID | Test description | Expected result | Actual result | Status |
|---|---|---|---|---|
| MT-01 | Create a new restaurant order | The order should be created successfully | Order created successfully | PASS |
| MT-02 | Verify order registration | The new order should appear in the application | Order appeared successfully | PASS |
| MT-03 | Change order status to delivered | Status should change to delivered | Status changed successfully | PASS |
| MT-04 | Change status after delivered | Application should prevent the change | Application prevented the change | PASS |
| MT-05 | Change order status to cancelled | Status should change to cancelled | Status changed successfully | PASS |
| MT-06 | Change status after cancelled | Application should prevent the change | Application prevented the change | PASS |
| MT-07 | Verify terminal status UI | Status selector disappears and final-status message is displayed | Status selector disappeared and message was displayed | PASS |

**Manual testing summary:** All seven recorded manual tests were successful. The application correctly created and registered orders, updated their statuses, and prevented changes after a terminal status (`delivered` or `cancelled`).

## 4. Evidence and Execution Notes

The group should preserve:
- Screenshot of the successful pytest result showing 18 passed.
- Screenshots of order creation and order registration.
- Screenshots showing delivered and cancelled terminal statuses.
- Screenshots showing the final-status interface message.

Record any additional test execution with its actual date, tester, actual result, and evidence.

Do not mark planned test cases as passed unless they have actually been executed.
