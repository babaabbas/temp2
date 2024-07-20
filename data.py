
from pymongo import MongoClient
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client["telegram_db"]
collection = db["users_db"]

def feedback_user_document(user_id, new_info):
    filter = {"user_id": user_id}
    update = {"$push": {"feedback": new_info}}
    result = collection.update_one(filter, update, upsert=True)

def upsert_user_document(user_id, new_info):
    filter = {"user_id": user_id}
    update = {"$push": {"info": new_info}}
    result = collection.update_one(filter, update, upsert=True)

import pymongo

def extract_info_from_mongodb(user_id):

    # Query MongoDB for the document with the given user_id
    query = {"user_id": user_id}
    document = collection.find_one(query)

    if not document:
        raise ValueError(f"No document found for user ID: {user_id}")

    # Extract the 'info' array from the document
    info_array = document.get("info", [])

    # Convert the array to a comma-separated string
    info_string = ", ".join(info_array)

    return info_string

# Example usage:
user_id = "1341414"
try:
    info_result = extract_info_from_mongodb(user_id)
    print(f"Info extracted for user ID {user_id}: {info_result}")
except ValueError as e:
    print(f"Error: {e}")

