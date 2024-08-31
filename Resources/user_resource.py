from flask import request, jsonify
from flask_restful import Resource
from Model.user import db, User  
from werkzeug.security import generate_password_hash
from flask_jwt_extended import JWTManager


jwt = JWTManager()

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if User.query.filter_by(email=email).first():
            return jsonify({"message": "Email already in use!"}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({"message": "Username already in use!"}), 400
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully!"}), 201
