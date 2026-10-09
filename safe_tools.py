"""
Week 6 Assignment: Safe Tools
Author: Your Name
Description: Implementation of error-catching utility functions.
"""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


if __name__ == "__main__":
    # Test cases matching the exact required output sequence
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_number("42"))
    print(safe_number("abc"))

    learner = {"name": "Kuku", "score": 82}
    print(get_field(learner, "score"))
    print(get_field(learner, "email"))