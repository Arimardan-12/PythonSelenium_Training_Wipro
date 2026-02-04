import requests
import pytest

@pytest.mark.parametrize("payload", [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25}
])
def test_add_patient(base_url, payload):
    res = requests.post(base_url, json=payload)
    assert res.status_code == 201

def test_get_patients(base_url):
    res = requests.get(base_url)
    assert res.status_code == 200

@pytest.mark.xfail
def test_invalid_patient(base_url):
    res = requests.post(base_url, json={"age": 20})
    assert res.status_code == 201
