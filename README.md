# PLP Python Week 6 Assignment

## File Descriptions
* **safe_tools.py**: Implements three error-handling functions (`safe_divide`, `safe_number`, and `get_field`) using `try / except` blocks to prevent application crashes.
* **README.md**: Overview of the assignment and explanation of runtime exceptions vs. syntax constraints.

## Conceptual Question
**Why can the if check not catch "abc" on its own?**
An `if` statement cannot catch an invalid type conversion (like trying to parse `int("abc")`) because the conversion triggers a runtime `ValueError` instantly when evaluated, crashing the program before the `if` statement can process it. Furthermore, code parsing errors (like syntax or indentation mistakes) are evaluated by Python before runtime even begins, making `try / except` blocks essential for handling predictable runtime exceptions cleanly.
