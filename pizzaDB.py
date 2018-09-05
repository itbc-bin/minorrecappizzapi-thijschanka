
from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {"name": "tonno"},
    {"name": "salami"},
    {"name": "HawaiISGeenPizzaHiervoorIsEenExtraRingVanHelGemaakt"}
]

@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({"pizzaDB":pizzaDB})

@app.route("/<string:name>", methods=["GET"])
def getonePizza(name):
    resultPizza = []
    for a in pizzaDB:
        if name in a.get("name"):
            resultPizza.append(a)

    return jsonify({'pizzaDB':resultPizza})



if __name__ == "__main__":
    app.run()