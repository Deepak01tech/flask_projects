from pymongo import MongoClient

client =None
student_collection=None
users_collection=None

def initialize_db(app):
    global client ,student_collection,users_collection

    client = MongoClient("mongodb://localhost:27017")

    db=client["Studenrecord"]
    student_collection=db["students"]
    users_collection=db["users"]
