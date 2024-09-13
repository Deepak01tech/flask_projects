from pymongo import MongoClient

client = None
books_collection = None

def initialize_db(app):
    global client, books_collection
    # Replace with your MongoDB URI
    #client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB
    client = MongoClient("mongodb+srv://dp55954:EuQ14nlgI8rFl1BQ@cluster0.klupu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB Atlas


    db = client["bookstore2"]  # Database name
    books_collection = db["books"]  # Collection name