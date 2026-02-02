from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

# 1. GET all movies
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200


# 2. GET movie by ID
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


# 3. POST add new movie
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    if not data or "id" not in data:
        return jsonify({"error": "Invalid data"}), 400

    movies.append(data)
    return jsonify(data), 201


# 4. PUT update movie
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.json
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


# 5. DELETE movie
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404


# 6. POST booking
@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.json
    movie_id = data.get("movie_id")
    tickets = data.get("tickets")

    for movie in movies:
        if movie["id"] == movie_id:
            total_price = movie["price"] * tickets
            booking = {
                "movie_id": movie_id,
                "tickets": tickets,
                "total_price": total_price
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Booking failed"}), 404


if __name__ == "__main__":
    app.run(debug=True)
