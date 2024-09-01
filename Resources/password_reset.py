from flask import current_app
from flask_restful import Resource, reqparse
import bcrypt
import jwt
from datetime import datetime, timedelta
from models import db, User
from flask_mail import Message

class RequestPasswordResetResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email is required')
        args = parser.parse_args()

        email = args['email']
        user = User.query.filter_by(email=email).first()

        if user is None:
            return {'error': 'Email not found'}, 404

        
        reset_token = jwt.encode(
            {'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)},
            current_app.config['JWT_SECRET_KEY'],
            algorithm='HS256'
        )

        user.reset_token = reset_token
        user.reset_token_expiration = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()

    
        msg = Message('Password Reset Request', recipients=[email])
        msg.body = f'Your password reset token is: {reset_token}'
        current_app.extensions['mail'].send(msg)

        return {'message': 'Password reset email sent'}, 200


class ResetPasswordResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('reset_token', type=str, required=True, help='Reset token is required')
        parser.add_argument('new_password', type=str, required=True, help='New password is required')
        args = parser.parse_args()

        reset_token = args['reset_token']
        new_password = args['new_password']

        try:
           
            payload = jwt.decode(reset_token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return {'error': 'Reset token has expired'}, 400
        except jwt.InvalidTokenError:
            return {'error': 'Invalid reset token'}, 400

        user_id = payload['user_id']
        user = User.query.get(user_id)

        if user is None or user.reset_token != reset_token or user.reset_token_expiration < datetime.utcnow():
            return {'error': 'Invalid or expired reset token'}, 400

        
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user.password = hashed_password
        user.reset_token = None
        user.reset_token_expiration = None
        db.session.commit()

        return {'message': 'Password has been reset successfully'}, 200
