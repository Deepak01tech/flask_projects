from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] ="dc6c3da671ac933dc1ba02eec2c2fa345e49f90e"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase3'


mongodb_client = PyMongo(app)
db = mongodb_client.db

from app import routes