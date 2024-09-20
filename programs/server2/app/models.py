from bson.objectid import ObjectId
from app import db

users_collection =db["users"]

def serialize_user(user):
    return {
        "_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }