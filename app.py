from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from Resources.user_resource import RegisterResource, LoginResource, LogoutResource
from flask_mail import Mail
from Resources.password_reset import RequestPasswordResetResource, ResetPasswordResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thread_and_trinket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'wekuraglorian07@gmail.com' 
app.config['MAIL_PASSWORD'] = 'wcuo lixb ceav ydao'  
app.config['MAIL_DEFAULT_SENDER'] = ('Thread and Trinket', 'wekuraglorian07@gmail.com')

mail = Mail(app)


db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
api = Api(app)




api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
api.add_resource(RequestPasswordResetResource, '/request-password-reset')
api.add_resource(ResetPasswordResource, '/reset-password')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
