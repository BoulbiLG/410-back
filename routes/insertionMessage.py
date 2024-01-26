from flask import Flask, current_app, request, Blueprint, jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
MONGO_URI = 'mongodb+srv://pierre:ztxiGZypi6BGDMSY@atlascluster.sbpp5xm.mongodb.net/410?retryWrites=true&w=majority'
app.config['MONGO_URI'] = MONGO_URI

mongo = PyMongo(app)

insertionMessage = Blueprint('insertionMessage', __name__)

@insertionMessage.route('/insertionMessage', methods=['POST'])
def insertion_Message():
    try:
        data = request.json

        pseudo = data.get('pseudo')
        message = data.get('message')

        print('pseudo : ', pseudo)
        print('message : ', message)

        date = datetime.now().strftime('%d %B %Y %H:%M')

        data_to_insert = {
            'date': date,
            'pseudo': pseudo,
            'message': message
        }

        mongo.db.msg.insert_one(data_to_insert)

        return jsonify({'success': True, 'message': 'Données insérées avec succès'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
