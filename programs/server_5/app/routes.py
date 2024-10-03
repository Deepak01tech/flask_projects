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


from bson import ObjectId


@main.route('/blog', methods=['GET'])
@token_required
def get_blogs(current_user):
    blogs = Blog.get_all_product()
    blogs_list = [{**blog,"id":str(blog["_id"])} for blog in blogs]
    return jsonify(blogs_list),200



@main.route('/blog/<blog_id>', methods=['GET'])
@token_required
def get_blog(current_user,blog_id):
    blog = Product.get_product_by_id(blog_id)
    if not blog:
        return jsonify({"message": "Blog not found"}), 404
    blog['_id']= str(blog['_id'])
    return jsonify(blog),200



