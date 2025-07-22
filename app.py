from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Global variable to store the latest sensor data
latest_data = {}

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    latest_data = request.get_json()
    latest_data['timestamp'] = datetime.utcnow().isoformat()
    print(f"Received at {latest_data['timestamp']} -", latest_data)
    return jsonify({"status": "ok"}), 200

@app.route('/latest', methods=['GET'])
def get_latest_data():
    if latest_data:
        return jsonify(latest_data), 200
    else:
        return jsonify({"message": "No data received yet"}), 404

@app.route('/', methods=['GET'])
def home():
    return "ESP32 Flask Server is running", 200
