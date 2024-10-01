from flask import Blueprint,request, jsonify
from .models import User, Product
from .auth import generate_token,token_required
from .import bcrypt

main = Blueprint('main', __name__)

@main.route('/signup',methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(data['email'], hashed_password)
    user.save()
    return jsonify({"message": "User created successfully"}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.get_user_by_email(data['email'])
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = generate_token(user.id)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid email or password"}), 401