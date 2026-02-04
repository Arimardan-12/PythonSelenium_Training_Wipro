from flask import Flask, request, jsonify, render_template, redirect
import json
import os

# ----------------------------
# PATH CONFIGURATION (IMPORTANT)
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "patients.json")

app = Flask(
    __name__,
    template_folder="../web/templates"
)

# ----------------------------
# INITIALIZE DATA FILE
# ----------------------------
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# ----------------------------
# WEB ROUTES
# ----------------------------
@app.route("/")
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    with open(DATA_FILE, "r") as f:
        patients = json.load(f)

    new_patient = {
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "contact": request.form["contact"],
        "disease": request.form["disease"],
        "doctor": request.form["doctor"]
    }

    # DUPLICATE CHECK (name + contact)
    for patient in patients:
        if patient["name"] == new_patient["name"] and patient["contact"] == new_patient["contact"]:
            return "❌ Patient already exists", 400

    patients.append(new_patient)

    with open(DATA_FILE, "w") as f:
        json.dump(patients, f, indent=4)

    return redirect("/patients_page")


@app.route("/patients_page")
def patients_page():
    with open(DATA_FILE, "r") as f:
        patients = json.load(f)

    return render_template("patients.html", patients=patients)


# ----------------------------
# API ROUTES
# ----------------------------
@app.route("/api/patients", methods=["GET"])
def get_patients():
    try:
        with open(DATA_FILE, "r") as f:
            patients = json.load(f)
        return jsonify(patients), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json

    with open(DATA_FILE, "r") as f:
        patients = json.load(f)

    patients.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(patients, f, indent=4)

    return jsonify({"message": "Patient added"}), 201


# ----------------------------
# RUN SERVER
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
