from flask import Flask, request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

senshies = [
    {'id':1, 'name': 'Tsukino Usagi', 'senshi': 'Sailor Moon', 'Guardian':'Love and Justice'},
    {'id':2, 'name': 'Mizuno Ami', 'senshi':'Sailor Mercury', 'Guardian': 'Water and Wisdom'},
    {'id':3, 'name': 'Hino Rei', 'senshi': 'Sailor Mars', 'Guardian':'Fire and Passion'},
    {'id':4, 'name':'Kino Makoto', 'senshi': 'Sailor Jupiter', 'Guardian':'Thunder and Courage'},
    {'id':5, 'name':'Aino Minako', 'senshi':'Sailor Venus', 'Guardian':'Love and Beauty'}
]

@app.route("/", methods=['GET'])
def hello():
    return "Sailor Moon API"

@app.route("/senshi/all", methods=['GET'])
def get_all_senshi():
    return jsonify(senshies)

@app.route("/senshi/<int:id>", methods=['GET'])
def find_senshi(id):
    results = []
    for senshi in senshies:
        if senshi['id'] == id:
            results.append(senshi)
    return jsonify(results)

app.run()