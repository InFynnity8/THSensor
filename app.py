from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(f"Received at {datetime.utcnow()} -", data)
    return jsonify({"status": "ok"}), 200

@app.route('/', methods=['GET'])
def home():
    return "ESP32 Flask Server is running", 200
