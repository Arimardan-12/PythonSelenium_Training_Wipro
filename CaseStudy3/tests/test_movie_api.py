import requests

def test_get_all_movies(base_url):
    response = requests.get(f"{base_url}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_movie(base_url):
    payload = {
        "id": 103,
        "movie_name": "Avatar",
        "language": "English",
        "duration": "2h 42m",
        "price": 280
    }
    response = requests.post(f"{base_url}/api/movies", json=payload)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Avatar"


def test_book_ticket(base_url):
    payload = {
        "movie_id": 101,
        "tickets": 2
    }
    response = requests.post(f"{base_url}/api/bookings", json=payload)
    assert response.status_code == 201
    assert response.json()["total_price"] == 500
