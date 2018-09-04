
from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {"name": "tonno"},
    {"name": "salami"},
    {"name": "HawaiISGeenPizzaHiervoorIsEenExtraRingVanHelGemaakt"}
]

@app.route("/", methods=['POST'])
def getPizza():
    return jsonify({"pizzaDB":pizzaDB})

if __name__ == "__main__":
    app.run()