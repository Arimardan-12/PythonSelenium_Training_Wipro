"""	Create application endpoints, Test API using Postman
	Using the Flask API created in Question 1:
	1. Test all endpoints using Postman End
	2. For each endpoint:
	Set the correct HTTP method , Send request headers (Content-Type: application/json) , Pass request body for POST
	3. Verify:
	Correct status codes (200, 201, 404)
	Correct JSON responses
	4. Document your Postman tests with:
	Screenshots (or steps)
	Sample request and response payloads"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Raj"}
]

# HOME ENDPOINT
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to User API"}), 200



# GET ALL USERS
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200



# GET USER BY ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404



# ADD NEW USER
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"]
    }
    users.append(new_user)

    return jsonify(new_user), 201



# DELETE USER
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"}), 200

    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
