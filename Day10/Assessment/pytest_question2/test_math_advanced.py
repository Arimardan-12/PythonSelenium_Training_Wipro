from test_math_operations import divide

# Use numbers fixture from conftest.py
def test_divide_with_numbers_fixture(numbers):
    a, b = numbers
    result = divide(a, b)
    assert result == 5

# Use module-scoped fixture
def test_resource(resource_setup):
    assert resource_setup == "RESOURCE READY"
