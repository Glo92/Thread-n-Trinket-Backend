from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from Model.User import db,User
from resources.user_resource import RegisterResource


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///thread_and_trinket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)
jwt = JWTManager(app)
api = Api(app)

api.add_resource(RegisterResource, '/register')

if __name__ == '__main__':
    app.run(port=5555, debug=True)