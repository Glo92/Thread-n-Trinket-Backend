from flask import request, jsonify
from flask_restful import Resource
from Model.user import db, User  # Import db and User from Model/user.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Initialize JWTManager
jwt = JWTManager()

# class RegisterResource(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
        
#         if User.query.filter_by(email=email).first():
#             return jsonify({"message": "Email already in use!"}), 400

#         if User.query.filter_by(username=username).first():
#             return jsonify({"message": "Username already in use!"}), 400
        
#         hashed_password = generate_password_hash(password, method='sha256')
#         new_user = User(username=username, email=email, password_hash=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
        
#         return jsonify({"message": "User registered successfully!"}), 201

# class LoginResource(Resource):
#     def post(self):
#         data = request.get_json()
#         email = data.get('email')
#         password = data.get('password')
        
#         user = User.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password_hash, password):
#             access_token = create_access_token(identity=email)
#             return jsonify(access_token=access_token), 200
        
#         return jsonify({"message": "Invalid credentials"}), 401

# class LogoutResource(Resource):
#     @jwt_required()
#     def post(self):
#         # No server-side logout functionality required for JWT.
#         return jsonify({"message": "Logout successful!"}), 200

# class UserInfoResource(Resource):
#     @jwt_required()
#     def get(self):
#         current_user = get_jwt_identity()
#         user = User.query.filter_by(email=current_user).first()
#         if user:
#             return jsonify({
#                 'username': user.username,
#                 'email': user.email,
#                 'is_admin': user.is_admin
#             }), 200
#         return jsonify({"message": "User not found"}), 404
