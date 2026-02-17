# FoodieApp

Simple Flask-based backend for restaurant, dish, user, order, and admin operations.

## Features
- Restaurant APIs: add, update, disable, get, search
- Dish APIs: add, update, toggle status, delete
- User APIs: register, basic search endpoint
- Order APIs: place order, add rating, view by user/restaurant
- Admin APIs: approve/disable restaurant, view feedback/orders
- Automated tests with `pytest` and Robot Framework

## Tech Stack
- Python
- Flask
- pytest
- Robot Framework (`robotframework`, `robotframework-requests`)

## Project Structure
```text
FoodieApp/
  app/
    routes/
    services/
    __init__.py
  tests/
    pytest/
      test_all.py
    robot/
      all_tests.robot
  run.py
  requirements.txt
  FoodieApp.postman_collection.json
```

## Setup
```powershell
cd C:\Users\Lenovo\PycharmProjects\PythonProject1\FoodieApp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run Application
```powershell
python run.py
```

By default, app runs at: `http://localhost:5000`

## Run Tests
Keep the Flask app running in one terminal, then run tests from another terminal.

### Pytest
```powershell
pytest tests\pytest -v
```

### Robot Framework
```powershell
robot tests\robot
```

## API Base URL
`http://localhost:5000/api/v1`

## Main Endpoints

### Restaurants
- `POST /restaurants/`
- `PUT /restaurants/{restaurant_id}`
- `PUT /restaurants/{restaurant_id}/dis`
- `GET /restaurants/{restaurant_id}`
- `GET /restaurants/search?name=&location=&dish=&rating=`

### Dishes
- `POST /dishes/`
- `PUT /dishes/{dish_id}`
- `PUT /dishes/{dish_id}/status`
- `DELETE /dishes/{dish_id}`

### Users
- `POST /users/register`
- `GET /users/search`

### Orders
- `POST /orders/`
- `POST /orders/ratings`
- `GET /orders/{user_id}`
- `GET /orders/restaurant/{restaurant_id}`

### Admin
- `PUT /admin/restaurants/{restaurant_id}/approve`
- `PUT /admin/restaurants/{restaurant_id}/disable`
- `GET /admin/feedback`
- `GET /admin/orders`

## Postman
Import `FoodieApp.postman_collection.json` into Postman for manual API testing.
