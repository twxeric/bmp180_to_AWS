from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_data = {}

@app.route('/data', methods=['POST'])
def post_data():
    global latest_data
    latest_data = request.get_json()
    return jsonify({"status": "success", "received": latest_data})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
