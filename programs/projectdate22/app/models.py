from db import db

class User(db.model):
    id = db.Column(db.Integer, primary_key=True,unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
