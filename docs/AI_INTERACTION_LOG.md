# AI Interaction Log

This log records the AI assistance used during the Homework 2 project. It documents the prompts, AI contributions, human review, and corrections made during development and testing.

| Date | Tool / model | Prompt or task | AI contribution | Human review / modification |
|---|---|---|---|---|
| 01/11/2026 | ChatGPT — GPT-6 | Help prepare and organize a Mini Restaurant Order Manager project for the homework. | Helped prepare the project structure, documentation, application files, and testing materials. | The project was extracted and configured on Windows. The team installed dependencies and reviewed the project files. |
| 01/11/2026 | ChatGPT — GPT-6 | Troubleshoot the Python error: `ModuleNotFoundError: No module named 'app'`. | Suggested checking the project directory and running pytest using `python -m pytest -v`. | The user checked the project files and executed the corrected command successfully. |
| 01/11/2026 | ChatGPT — GPT-6 | Improve the automated tests for order creation, validation, retrieval, and status management. | Generated additional pytest test cases covering valid input, invalid input, boundary conditions, and terminal order statuses. | The user integrated the tests into `tests/test_orders.py` and executed them locally. |
| 01/11/2026 | ChatGPT — GPT-6 | Troubleshoot an ImportError involving `OrderService`. | Helped identify that test code had accidentally been placed in `app/order_service.py` instead of `tests/test_orders.py`. | The user restored the correct application service code and kept the test code in its proper file. |
| 01/11/2026 | ChatGPT — GPT-6 | Fix a SyntaxError caused by Markdown code fences in a Python file. | Explained that the Markdown markers ` ```python ` and ` ``` ` must not be included in Python source code. | The user removed the extra markers and saved the corrected file. |
| 01/11/2026 | ChatGPT — GPT-6 | Verify the automated tests and run the application. | Provided instructions for running pytest and starting the Flask application. | The user executed the tests and confirmed 18 passed and 0 failed. |
| 01/11/2026 | ChatGPT — GPT-6 | Verify order status rules through manual testing. | Suggested testing terminal statuses and checking whether further status changes are prevented. | The user tested the application and confirmed that changing an order after `delivered` or `cancelled` was prevented. |
| 01/11/2026 | ChatGPT — GPT-6 | Improve project documentation and update testing results. | Helped update README.md, TEST_PLAN.md, and TEST_CASES.md to reflect the latest test results. | The user reviewed and integrated the updated documentation. |
| 18/11/2026 | ChatGPT — GPT-6 | Review the homework instructions and repository, then improve the implementation against the specification. | Identified the one-item-only browser form, unrestricted status jumps, stale reported test counts, and pytest collection failure caused by the test filename. Implemented multi-item entry, explicit status transitions, relevant tests, and documentation updates. | The user should review the changes, run the app in a browser, and retain this interaction as evidence; the team should add its own contributions and actual observations. |

## AI Limitations and Human Responsibility

- AI-generated code and documentation must be reviewed by the development team.
- An incorrect file placement caused an ImportError during testing.
- Markdown code fences copied into a Python file caused a SyntaxError.
- AI-generated code cannot be considered correct without execution and verification.
- The team is responsible for understanding and validating the application.
- Automated test results must be checked in the actual development environment.
- Manual testing is necessary in addition to automated testing.
- The team must document any incorrect, incomplete, or unsuitable AI-generated output discovered during development.

## Evidence to Preserve

- Exact prompts used by each team member.
- AI-generated code and suggestions.
- Human code modifications and Git commits.
- Automated test output showing the latest actual result (21 passed after the 18/11/2026 changes).
- Screenshots of successful manual tests.
- Evidence of bugs, corrections, and limitations discovered during testing.

## Team Contributions

Each team member must add their actual AI interactions and contributions to this log.

Do not claim that an AI interaction occurred unless it actually happened. The current log documents the interactions recorded during this development process; it does not replace the individual contributions of the other group members.
