from flask import Flask, request, jsonify
from sqlalchemy import create_engine


app = Flask(__name__)
app.config["DEBUG"] = True
db_connection = create_engine('sqlite:////Users/momol/SideProjects/mcu-api/mcu.db') #database url


#endpoint for mainpage
@app.route("/", methods=['GET'])
def mainPage():
    return "Sailor Moon API"

#endpoint to get all superheroes
@app.route("/superheroes/all", methods=['GET'])
def get_all_superheroes():
    conn = db_connection.connect() # connect to database
    query = conn.execute("SELECT * FROM superheroes") #executing query
    results = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor] #parsing through query
    return jsonify(results)

#endpoint to get a superheroes with a given name
@app.route("/superheroes/name/<string:name>", methods=['GET'])
def find_superhero_via_name(name):
    """
        returns data of a superhero with a given name
    """
    conn = db_connection.connect()
    sql = "SELECT * FROM superheroes WHERE name = '%s'" %(name)
    query = conn.execute(sql)
    results = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
    return jsonify(results)

#endpoint to get a superheroes with a given alias
@app.route("/superheroes/alias/<string:alias>", methods=['GET'])
def find_superhero_via_alias(alias):
    """
        returns data of a superhero with a given alias
    """
    conn = db_connection.connect()
    sql = "SELECT * FROM superheroes WHERE name = '%s'" %(alias)
    query = conn.execute(sql)
    results = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
    return jsonify(results)

#endpoint to get all superheroes of a species
@app.route("/superheroes/species/<string:species>", methods=['GET'])
def get_all_species(species):
    """
        returns data of a superheroes of a given species
    """
    conn = db_connection.connect()
    sql = "SELECT * FROM superheroes WHERE species = '%s'" %(species)
    query = conn.execute(sql)
    results = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
    return jsonify(results)
