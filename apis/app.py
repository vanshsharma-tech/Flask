from flask import Flask, jsonify
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

if db.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")

@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})


@app.route("/get-records")
def get_records():
    # Placeholder for record retrieval logic
    return jsonify({"message": "Records retrieved successfully!"})


@app.route("/get-single-record/<int:record_id>")
def get_single_record(record_id):
    # Placeholder for single record retrieval logic
    return jsonify({"message": f"Record with ID {record_id} retrieved successfully!"})


@app.route("/create", methods=["POST", "GET"])
def create():
    # Placeholder for record creation logic
    return jsonify(
        {
            "student_id": 1,
            "name": "John Doe",
            "message": "New account created successfully!"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
