import pytest

# Fixture for numbers (function scope)
@pytest.fixture(scope="function")
def numbers():
    print("\n[FIXTURE] Providing test numbers")
    return (10, 2)

# Fixture for module-level resource (module scope)
@pytest.fixture(scope="module")
def resource_setup():
    print("\n[FIXTURE] Setting up module-level resource")
    yield "RESOURCE READY"
    print("\n[FIXTURE] Tearing down module-level resource")
