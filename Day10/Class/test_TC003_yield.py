
import pytest

@pytest.mark.smoke
def test_smoke1():
    assert True

@pytest.fixture()
def setup_teardown():
    print("setup")
    yield
    print("Teardown")


def test_example(setup_teardown):
    print("test running")

def test_example1(setup_teardown):
    print("test2 running")