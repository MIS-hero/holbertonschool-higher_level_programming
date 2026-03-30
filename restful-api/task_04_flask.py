from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    if username in users: 
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user",  methods=["POST"])
def add_user():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if "username" not in data:
        return jsonify({"error":"Username is required"}),400
    if data["username"] in users:
        return jsonify({"error":"Username already exists"}),409
    users[data["username"]] = data
    return jsonify(data), 201
if __name__ == "__main__": app.run()