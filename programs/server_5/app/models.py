from bson import ObjectId
from flask_login import UserMixing
from .import mongo,bcrypt

# User Model

class User(UserMixing):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.email = user_data['email']
        self.password = user_data['password']

    @staticmethod
    def create_user(data):
        hased_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        data['password'] = hased_password
        return mongo.db.users.find_one({"email":email})
        