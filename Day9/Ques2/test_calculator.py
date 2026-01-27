"""Question 2 – Unit Testing & Test Driven Development (TDD)

Topics Covered:
Unit testing, Test Driven Development

Implement Test Driven Development (TDD) for a simple calculator module.

Requirements:

1. Write unit test cases first for operations:



Addition

Subtraction

Multiplication

Division

2. Use a Python unit testing framework (unittest or pytest)

3. Implement the calculator functions to make the tests pass

4. Demonstrate handling of edge cases (e.g., division by zero)

5. Explain the TDD cycle: Red → Green → Refactor

"""

import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiplication():
    assert multiply(4, 3) == 12
    assert multiply(0, 5) == 0

def test_division():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
