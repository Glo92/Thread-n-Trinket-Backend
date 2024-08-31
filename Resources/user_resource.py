from flask_restful import Resource, reqparse
import bcrypt
from flask_mail import Message
from flask import current_app, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended import unset_jwt_cookies
from models import db, User

class RegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is required')
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        username = args['username']
        email = args['email']
        password = args['password']

        if User.query.filter_by(username=username).first():
            return {'error': 'Username already exists'}, 400

        if User.query.filter_by(email=email).first():
            return {'error': 'Email already exists'}, 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Send an email upon successful registration
        msg = Message(subject="Registration Successful",
                      recipients=[email],  # The user's email
                      body=f"Hello {username},\n\nWelcome to Thread and Trinket! You have successfully registered.")
        current_app.extensions['mail'].send(msg)

        return {'message': 'User registered successfully and email sent'}, 201


class LoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        email = args['email']
        password = args['password']

        user = User.query.filter_by(email=email).first()

        if user is None:
            return {'error': 'Invalid email or password'}, 401

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return {'error': 'Invalid email or password'}, 401

        # Generate a JWT token
        access_token = create_access_token(identity=user.id)

        return {'message': 'Login successful', 'access_token': access_token}, 200


class LogoutResource(Resource):
    @jwt_required()
    def post(self):
        response = jsonify({"message": "Logout successful"})
        unset_jwt_cookies(response)  # Unset the JWT cookies to log out
        return response




# from flask_restful import Resource, reqparse
# import bcrypt
# from flask import jsonify
# from flask_jwt_extended import jwt_required,create_access_token, get_jwt, get_jwt_identity
# from flask_jwt_extended import unset_jwt_cookies
# from models import db, User

# class RegisterResource(Resource):
#     def post(self):
        
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str, required=True, help='Username is required')
#         parser.add_argument('email', type=str, required=True, help='Email is required')
#         parser.add_argument('password', type=str, required=True, help='Password is required')
#         args = parser.parse_args()

        
#         username = args['username']
#         email = args['email']
#         password = args['password']

        
#         if User.query.filter_by(username=username).first():
#             return {'error': 'Username already exists'}, 400

        
#         if User.query.filter_by(email=email).first():
#             return {'error': 'Email already exists'}, 400

       
#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        
#         user = User(username=username, email=email, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()

        
#         return {'message': 'User registered successfully'}, 201


# class LoginResource(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('email', type=str, required=True, help='Email is required')
#         parser.add_argument('password', type=str, required=True, help='Password is required')
#         args = parser.parse_args()

#         email = args['email']
#         password = args['password']

#         user = User.query.filter_by(email=email).first()

#         if user is None:
#             return {'error': 'Invalid email or password'}, 401

#         if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
#             return {'error': 'Invalid email or password'}, 401

#         # Generate a JWT token
#         access_token = create_access_token(identity=user.id)

#         return {'message': 'Login successful', 'access_token': access_token}, 200
    
# class LogoutResource(Resource):
#     @jwt_required()
#     def post(self):
#         response = jsonify({"message": "Logout successful"})
#         unset_jwt_cookies(response)  # Unset the JWT cookies to log out
#         return response