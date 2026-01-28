from auth import login

def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"

def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"
