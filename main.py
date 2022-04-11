from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data" : data,
        "message" : "success"
    }), 200


@app.route("/planet")

def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)

    return jsonify({
        "data" : planet_data,
        "message" : "success"
    }),200

# 11 Comae Berenices b

if __name__ == "__main__":
    app.run()


# http://127.0.0.1:5000/planet?name=11%20Comae%20Berenices%20b
