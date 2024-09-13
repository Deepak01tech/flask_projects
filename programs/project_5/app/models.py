from pymongo import MongoClient

client = None
books_collection = None
users_collection = None

def initialize_db(app):
    global client, books_collection, users_collection

    client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB

    db = client["bookstore"]  # Database name
    books_collection = db["books"]  # Collection for books
    users_collection = db["users"]  # Collection for users