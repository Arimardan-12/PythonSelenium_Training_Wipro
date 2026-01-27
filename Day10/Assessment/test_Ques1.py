"""Question 1 – Pytest Basics, Test Discovery & Assertions c Pytest overview, Test discovery, Writing and running unit tests, Assert statements and exceptions Requirements:
1. Write unit tests using Pytest conventions (test_*.py, test_ functions)
2. Demonstrate automatic test discovery
3. Use assert statements to validate results
4. Write a test to validate that an exception is raised for division by zero 5. Execute tests using the pytest command"""

import pytest

# Function to test
def divide(a, b):
    return a / b

def add(a, b):
    return a + b

# 1. Test addition
def test_add():
    result = add(5, 3)
    assert result == 8  # Checks the correct sum

# 2. Test division
def test_divide():
    result = divide(10, 2)
    assert result == 5  # Checks correct division

# 3. Test division by zero exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):  # Checks exception
        divide(10, 0)
