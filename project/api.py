from flask import Flask, request,abort, render_template
from project.implementations import *

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False

#endpoint for mainpage
@app.route("/", methods=['GET'])
def mainPage():
    return render_template('index.html')

#endpoint for about page
@app.route("/about", methods=['GET'])
def aboutPage():
        return render_template('about.html')

#endpoint for documentation page
@app.route("/docs", methods=["GET"])
def docsPage():
        return render_template('docs.html')

#endpoint to get all characters
@app.route("/characters", methods=['GET'])
def get_characters():
    return get_all_characters()

#endpoint to get a specific character based on name
@app.route("/character/<string:name>", methods=['GET'])
def get_character(name):
        return_characters =  get_specific_character(name)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="character not found") 

#endpoint to filter characters based on bending
@app.route("/characters/benders/<string:bending>", methods=['GET'])
def get_characters_bending(bending):
        return get_benders(bending)

#endpoint to filter characters based on gender
@app.route("/characters/gender/<string:gender>", methods=["GET"])
def get_characters_gender(gender):
        return get_gender(gender)

#endpoint to filter characters based on ethnicity
@app.route("/characters/ethnicity/<string:ethnicity>", methods=["GET"])
def get_characters_ethnicity(ethnicity):
        return get_ethnicity(ethnicity)

#endpoint to filter characters based on nationality
@app.route("/characters/nationality/<string:nationality>", methods=["GET"])
def get_characters_nationality(nationality):
        return get_nationality(nationality)

#endpoint to filter characters based on affiliation
@app.route("/characters/affiliations/<string:affiliation>", methods=["GET"])
def get_characters_affiliation(affiliation):
        return get_affiliation(affiliation)

#endpoint to get all locations
@app.route("/locations", methods=["GET"])
def get_locations():
        return get_all_locations()

#endpoint to filter locations based on nation
@app.route("/locations/nation/<string:nation>", methods=["GET"])
def get_locations_nation(nation):
        return get_nation(nation)

#error handling message
@app.errorhandler(404)
def resource_not_found(e):
        return jsonify(error=str(e)), 404
        