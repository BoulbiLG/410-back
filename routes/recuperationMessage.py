from flask import Flask, current_app, request, Blueprint, jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
MONGO_URI = 'mongodb+srv://pierre:ztxiGZypi6BGDMSY@atlascluster.sbpp5xm.mongodb.net/410?retryWrites=true&w=majority'
app.config['MONGO_URI'] = MONGO_URI

mongo = PyMongo(app)

recuperationMessage = Blueprint('recuperationMessage', __name__)

@recuperationMessage.route('/recuperationMessage', methods=['GET'])
def recuperation_Message():
    try:
        
        messages = list(mongo.db.msg.find({}, {'_id': 0}))

        return jsonify({'success': True, 'messages': messages})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})





        
