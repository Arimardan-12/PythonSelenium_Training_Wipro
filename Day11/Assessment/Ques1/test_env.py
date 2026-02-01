import pytest

def test_environment(env):
    print(f"Running tests in {env} environment")
    assert env in ["dev", "qa", "prod"]


@pytest.mark.skip(reason="Feature not implemented yet")
def test_skip_example():
    assert 1 == 2


@pytest.mark.xfail(reason="Known bug: division by zero")
def test_expected_failure():
    x = 1 / 0
