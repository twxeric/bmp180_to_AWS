from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Allows access from browser and other domains

latest_data = {}

@app.route('/data', methods=['POST'])
def post_data():
    global latest_data
    latest_data = request.get_json()
    return jsonify({"status": "success", "received": latest_data})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
