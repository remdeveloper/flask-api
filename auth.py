from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint('auth', __name__) #create Blueprint named auth

@auth.route('/register', methods=['POST']) 
def register():
    data = request.get_json() # parse json from request body
    username = data.get('username') # retrieve user name field
    password = data.get('password') # retrieve password field

    if User.query.filter_by(username=username).first(): # check if username already exists
        return jsonify({"message": "User already exists"}), 400 # return an error if username exists

    hashed_password = generate_password_hash(password) # hash the password
    new_user = User(username=username, password=hashed_password) # creates a new user object
    db.session.add(new_user) # add user to database
    db.session.commit() # save user to database

    return jsonify({"message": "User registered successfully"}), 201 # confirm successful registration

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json() # parse json from request body
    username = data.get('username') # retrieve username field
    password = data.get('password') # retrieve password field

    user = User.query.filter_by(username=username).first() #find user by username

    if not user or not check_password_hash(user.password, password): # validate the username and password
        return jsonify({"message": "Invalid credentials"}), 401 #return an error if invalid
    
    access_token = create_access_token(identity=str(user.id)) # generate JWT token for user
    return jsonify({"access_token": access_token}), 200 #return the token to the client

@auth.route('/users', methods=['GET'])
@jwt_required() # a JWT token is required
def get_users():
    users = User.query.all() # fetch all users from the database
    return jsonify([{"id": user.id, "username": user.username} for user in users]), 200 # return a list of users

@auth.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"message": "User not found"}), 404

    user.username = data.get('username', user.username) # update username
    if 'password' in data: # update password
        user.password = generate_password_hash(data['password'])
    db.session.commit() # save changes to database

    return jsonify({"message": "User updated successfully"}), 200

@auth.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    
    if not user: # check if user exists in database
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(user) # delete user
    db.session.commit() # save changes
    return jsonify({"message": "User deleted successfully"}), 200

@auth.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user: # check if user exists
        return jsonify({"message": "User not found"}), 404
    return jsonify({"id": user.id, "username": user.username}), 200
