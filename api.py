from flask import Flask, request,abort
from flask_api import status
from character import *

app = Flask(__name__)
app.config["DEBUG"] = True

#endpoint for mainpage
@app.route("/", methods=['GET'])
def mainPage():
    return "Avatar the Last Airbender API"

@app.route("/characters", methods=['GET'])
def get_characters():
    return all()

@app.route("/character/<string:name>", methods=['GET'])
def get_character(name):
        return character(name)

@app.route("/characters/<string:filter>", methods=['GET'])
def get_character_filter(filter):
        filters = charactersFilter()
        if filter in filters.get_bendings():
                print("pass2")
                return benders(filter)
        elif filter in filters.get_genders():
                print("pass3")
                return gender(filter)
        elif filter in filters.get_ethnicity():
                print("pass1")
                return ethnicity(filter)

        else:
                abort(404, description="Filter not found") 

@app.errorhandler(404)
def resource_not_found(e):
        return jsonify(error=str(e)), 404
        