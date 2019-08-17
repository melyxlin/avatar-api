from flask import Flask, request,abort, render_template
from character import *

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False

#endpoint for mainpage
@app.route("/", methods=['GET'])
def mainPage():
    return render_template('index.html')

@app.route("/characters", methods=['GET'])
def get_characters():
    return all_characters()

@app.route("/character/<string:name>", methods=['GET'])
def get_character(name):
        return character(name)

@app.route("/characters/<string:filter>", methods=['GET'])
def get_character_filter(filter):
        filters = charactersFilter()
        if filter in filters.get_bendings():
                return benders(filter)
        elif filter in filters.get_genders():
                return gender(filter)
        elif filter in filters.get_element():
                return element(filter)
        else:
                abort(404, description="Filter not found") 

@app.errorhandler(404)
def resource_not_found(e):
        return jsonify(error=str(e)), 404
        