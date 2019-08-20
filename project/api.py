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
@app.route("/characters/<string:name>", methods=['GET'])
def get_character(name):
        return_character =  get_specific_character(name)
        if return_character != None:
                return return_character
        else:
                abort(404, description="characters not found") 

#endpoint to filter characters based on bending
@app.route("/characters/benders/<string:bending>", methods=['GET'])
def get_characters_bending(bending):
        return_characters =  get_benders(bending)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="characters not found") 

#endpoint to filter characters based on gender
@app.route("/characters/gender/<string:gender>", methods=["GET"])
def get_characters_gender(gender):
        return_characters = get_gender(gender)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="characters not found") 

#endpoint to filter characters based on ethnicity
@app.route("/characters/ethnicity/<string:ethnicity>", methods=["GET"])
def get_characters_ethnicity(ethnicity):
        return_characters = get_ethnicity(ethnicity)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="characters not found") 

#endpoint to filter characters based on nationality
@app.route("/characters/nationality/<string:nationality>", methods=["GET"])
def get_characters_nationality(nationality):
        return_characters = get_nationality(nationality)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="characters not found") 

#endpoint to filter characters based on affiliation
@app.route("/characters/affiliations/<string:affiliation>", methods=["GET"])
def get_characters_affiliation(affiliation):
        return_characters = get_affiliation(affiliation)
        if return_characters != None:
                return return_characters
        else:
                abort(404, description="characters not found") 

#endpoint to get all locations
@app.route("/locations", methods=["GET"])
def get_locations():
        return get_all_locations()

#endpoint to filter locations based on nation
@app.route("/locations/nation/<string:nation>", methods=["GET"])
def get_locations_nation(nation):
        return_nations = get_nation(nation)
        if return_nations != None:
                return return_nations
        else:
                abort(404, description="bending not found") 

#endpoint to get all bendings
@app.route("/bendings", methods=["GET"])
def get_bendings():
        return get_all_bendings()

@app.route("/bendings/<string:name>", methods=["GET"])
def get_bending(name):
        return_bending = get_specific_bending(name)
        if return_bending != None:
                return return_bending
        else:
                abort(404, description="bending not found") 

#error handling message
@app.errorhandler(404)
def resource_not_found(e):
        return jsonify(error=str(e)), 404
        