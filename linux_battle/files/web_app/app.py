from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
LEADERBOARD_FILE = "/var/log/leaderboard.json"

@app.route("/")
def home():
    return "<h1>Linux Battle Royale Leaderboard</h1><p>Go to /leaderboard to see rankings.</p>"

@app.route("/leaderboard")
def leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            data = json.load(f)
        return jsonify({"leaderboard": data})
    return jsonify({"error": "No leaderboard data found!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
