"""	Question 2 – Setup/Teardown, Fixtures & conftest.py
	Enhance the test suite created in Question 1.
	Requirements:
	1. Implement xUnit-style methods (setup_module, teardown_module, setup_function, teardown_function)
	2. Create reusable fixtures for test data and resources
	3. Move common fixtures to a conftest.py file
	4. Demonstrate fixture scope (function, module)
	5. Use fixtures in multiple test file			"""


import pytest

# Functions to test
def divide(a, b):
    return a / b

def add(a, b):
    return a + b

# ----------------------------
# xUnit-style setup/teardown
# ----------------------------
def setup_module(module):
    print("\n[SETUP MODULE] Starting all tests in this module")

def teardown_module(module):
    print("\n[TEARDOWN MODULE] Finished all tests in this module")

def setup_function(function):
    print(f"[SETUP FUNCTION] Starting test: {function.__name__}")

def teardown_function(function):
    print(f"[TEARDOWN FUNCTION] Finished test: {function.__name__}")

# ----------------------------
# Tests using assert statements
# ----------------------------
def test_add():
    result = add(5, 3)
    assert result == 8

def test_divide():
    result = divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

