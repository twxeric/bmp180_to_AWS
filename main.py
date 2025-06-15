from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Lista donde se guardarán las lecturas
data_log = []

@app.route('/data', methods=['POST'])
def post_data():
    incoming = request.get_json()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "timestamp": timestamp,
        "temperature": incoming.get("temperature"),
        "pressure": incoming.get("pressure"),
        "altitude": incoming.get("altitude")
    }
    data_log.append(entry)
    return jsonify({"status": "success", "data": entry})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_log)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
