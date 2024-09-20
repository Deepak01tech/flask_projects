from flask import Flask
from pymongo import MongoClient
from app.config import MONGODB_URI
from  flask_cors import CORS


app = Flask(__name__)
CORS(app)
client = MongoClient(MONGODB_URI)
db= client["flaskdb"]

from app .routes import *

def create_app():
    app = Flask(__name__)
    return app
