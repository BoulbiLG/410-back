import sys
from webbrowser import register
from pymongo import MongoClient
import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content, Accept, Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    return response

app.after_request(after_request)

app.debug = False
CORS(app, resources={r"*": {"origins": "*"}})


from routes.insertionMessage import insertionMessage
from routes.recuperationMessage import recuperationMessage


#=========================================== INITIALISATION DU SERVEUR TERMINE ===============================================#


# compte
app.register_blueprint(insertionMessage)
app.register_blueprint(recuperationMessage)


#===========================================LANCEMENT DU SERVER===============================================#
if __name__ == '__main__':
    url = "mongodb+srv://pierre:ztxiGZypi6BGDMSY@atlascluster.sbpp5xm.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(url, connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1)
    collection = client.db["things"]
    app.run(host='0.0.0.0', port=1234)