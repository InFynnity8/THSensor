from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store the latest data in memory (you can later change this to a database)
latest_data = {}

@app.route('/data', methods=['POST', 'GET'])
def handle_data():
    global latest_data

    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No JSON received"}), 400

            # Log and store the data
            latest_data = data
            print("Received:", latest_data)
            return jsonify({"message": "Data received", "data": latest_data}), 200

        except Exception as e:
            print("Error:", e)
            return jsonify({"error": "Failed to process data"}), 500

    elif request.method == 'GET':
        # Return the last received sensor data
        if latest_data:
            return jsonify(latest_data), 200
        else:
            return jsonify({"message": "No data available"}), 404

if __name__ == '__main__':
    app.run(debug=True)
