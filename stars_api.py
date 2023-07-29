from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

# To display data of all the stars
@app.route("/")
def index():
    return jsonify({
        "data" : data,
        "message": "success"
    }), 200

# To display data of specified stars
@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()