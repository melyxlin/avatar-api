from flask import Flask, request,abort, render_template
from character import *
from locations import *

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False

#endpoint for mainpage
@app.route("/", methods=['GET'])
def mainPage():
    return render_template('index.html')

@app.route("/about", methods=['GET'])
def docPage():
        return render_template('about.html')

@app.route("/characters", methods=['GET'])
def get_characters():
    return get_all_characters()

@app.route("/character/<string:name>", methods=['GET'])
def get_character(name):
        return_characters =  get_specific_character(name)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="character not found") 


@app.route("/characters/bending/<string:bending>", methods=['GET'])
def get_characters_bending(bending):
        return get_benders(bending)

@app.route("/characters/gender/<string:gender>", methods=["GET"])
def get_characters_gender(gender):
        return get_gender(gender)

@app.route("/characters/ethnicity/<string:ethnicity>", methods=["GET"])
def get_characters_ethnicity(ethnicity):
        return get_ethnicity(ethnicity)

@app.route("/characters/nationality/<string:nationality>", methods=["GET"])
def get_characters_nationality(nationality):
        return get_nationality(nationality)

@app.route("/characters/affliaition/<string:affliation>", methods=["GET"])
def get_characters_affiliation(affiliation):
        return get_affiliation(affiliation)

@app.route("/locations", methods=["GET"])
def get_locations():
        return get_all_locations()

@app.route("/locations/nation/<string:nation>", methods=["GET"])
def get_locations_nation(nation):
        return get_locations_nation()

@app.errorhandler(404)
def resource_not_found(e):
        return jsonify(error=str(e)), 404
        