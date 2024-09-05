from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from flask_mail import Mail

app = Flask(__name__)

# Configuration
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

# Import resources
from Resources.user_resource import RegisterResource, LoginResource, LogoutResource
from Resources.password_reset import RequestPasswordResetResource, ResetPasswordResource
from Resources.products import ProductResource, ProductListResource, ProductUpdateResource, ProductDeleteResource, ProductDetailResource
from Resources.category import CategoryResource, CategoryListResource, CategoryUpdateResource, CategoryDeleteResource
from Resources.cart_resource import AddToCartResource, ViewCartResource, UpdateCartResource, RemoveFromCartResource
from Resources.order_resource import OrderResource

# Add resources to API
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
api.add_resource(RequestPasswordResetResource, '/request-password-reset')
api.add_resource(ResetPasswordResource, '/reset-password')

api.add_resource(ProductResource, '/products')
api.add_resource(ProductListResource, '/products')
api.add_resource(ProductDetailResource, '/products/<int:product_id>')
api.add_resource(ProductUpdateResource, '/products/<int:product_id>')
api.add_resource(ProductDeleteResource, '/products/<int:product_id>')

api.add_resource(CategoryResource, '/categories')
api.add_resource(CategoryListResource, '/categories')
api.add_resource(CategoryUpdateResource, '/categories/<int:category_id>')
api.add_resource(CategoryDeleteResource, '/categories/<int:category_id>')


api.add_resource(AddToCartResource, '/cart/add')
api.add_resource(ViewCartResource, '/cart/view')
api.add_resource(UpdateCartResource, '/cart/update')
api.add_resource(RemoveFromCartResource, '/cart/remove')


api.add_resource(OrderResource, '/orders', '/orders/<int:order_id>')

if __name__ == '__main__':
    app.run(debug=True)

