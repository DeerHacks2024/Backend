from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)

CORS(app)

host = os.environ["DB_HOST"]
password = os.environ["DB_PASSWORD"]
username = os.environ["DB_USERNAME"]

mongodb_uri = f'mongodb+srv://{username}:{password}@{host}.pfxfbes.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongodb_uri)
db = client['DeerHacks2024']

collection = db['DeerHacks2024']

@app.route('/')
def index():
    return 'DeerHacks 2024'

@app.route('/retrieve', methods=['GET'])
def retrieve_data():
    # Retrieve data from MongoDB
    data = list(collection.find())

    # Convert ObjectId to string for JSON serialization
    serialized_data = []
    for entry in data:
        entry['_id'] = str(entry['_id'])
        serialized_data.append(entry)

    return jsonify({"data": serialized_data})

@app.route('/retrieve/<category>', methods=['GET'])
def retrieve_data_by_category(category):
    # Retrieve data from MongoDB
    data = list(collection.find({"category": category}))

    # Convert ObjectId to string for JSON serialization
    serialized_data = []
    for entry in data:
        entry['_id'] = str(entry['_id'])
        serialized_data.append(entry)

    return jsonify({"data": serialized_data})

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.get_json()

    # Insert data into MongoDB
    result = collection.insert_one(data)

    return jsonify({"message": "Data inserted successfully", "inserted_id": str(result.inserted_id)})

@app.route('/add-attendee', methods=['POST'])
def add_attendee():
    data = request.get_json()

    # Assuming the request includes the _id of the event and the attendee name
    event_id = data.get('_id')
    attendee_name = data.get('attendee')

    if not event_id or not attendee_name:
        return jsonify({"error": "Invalid request format"}), 400

    # Insert data into MongoDB
    result = collection.update_one(
        {"_id": ObjectId(event_id)},
        {"$push": {"attendees": attendee_name}}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Event not found"}), 404

    return jsonify({"message": "Attendee added successfully", "updated_id": str(result.upserted_id)})

@app.route('/update', methods=['POST'])
def update_data():
    data = request.get_json()

    # Update data in MongoDB
    result = collection.update_one({"_id": ObjectId(data['_id'])}, {"$set": data})

    return jsonify({"message": "Data updated successfully", "modified_count": result.modified_count})

@app.route('/delete', methods=['DELETE'])
def delete_data():
    data = request.get_json()

    # Delete data from MongoDB
    result = collection.delete_one(data)

    return jsonify({"message": "Data deleted successfully", "deleted_count": result.deleted_count})

@app.route('/delete/<id>', methods=['DELETE'])
def delete_data_by_id(id):
    # Delete data from MongoDB
    result = collection.delete_one({"_id": ObjectId(id)})

    return jsonify({"message": "Data deleted successfully", "deleted_count": result.deleted_count})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0",port=5000)