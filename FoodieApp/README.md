# FoodieApp 

## Setup
1. python -m venv venv
2. Activate venv:
   - Windows: venv\Scripts\activate
   - Linux/Mac: source venv/bin/activate
3. pip install -r requirements.txt

## Run Flask App
python run.py

## Run Pytest Tests
pytest tests/pytest -v

## Run Robot Framework Tests
robot tests/robot

## Manual Testing
Import FoodieApp.postman_collection.json into Postman