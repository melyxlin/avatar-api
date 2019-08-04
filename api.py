from flask import Flask, request, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["DEBUG"] = True
db_connection = create_engine('sqlite:////Users/momol/SideProjects/sailor-moon-api/sailormoon.db') #database url

@app.route("/", methods=['GET'])
def mainPage():
    """
        main page
    """
    return "Sailor Moon API"

@app.route("/senshi/all", methods=['GET'])
def get_all_senshi():
    """
        returns all senshies
    """
    conn = db_connection.connect() # connect to database
    query = conn.execute("SELECT * FROM Senshi") #executing query
    results = {'data':[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} #parsing through query
    return jsonify(results)

@app.route("/senshi/<int:id>", methods=['GET'])
def find_senshi(id):
    """
        returns data of a senshi with a given id
    """
    conn = db_connection.connect()
    query = conn.execute("SELECT * FROM Senshi WHERE SenshiId = %d" %int(id))
    results = {'data':[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return jsonify(results)