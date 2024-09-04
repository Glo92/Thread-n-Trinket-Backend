from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import UserMixin
from datetime import datetime

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reset_token = db.Column(db.String(255), nullable=True)
    reset_token_expiration = db.Column(db.DateTime, nullable=True)
    
    orders = db.relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'reset_token': self.reset_token,
            'reset_token_expiration': self.reset_token_expiration.isoformat() if self.reset_token_expiration else None
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', back_populates='products')

    order_items = db.relationship('OrderItem', back_populates='product')
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'category_id': self.category_id
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    products = db.relationship('Product', back_populates='category')

    def __repr__(self):
        return f'<Category {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable to accommodate non-authenticated users
    session_id = db.Column(db.String(255), nullable=True)  # New field for session-based carts
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', back_populates='carts')

    def __repr__(self):
        return f'<Cart {self.id} for User {self.user_id} or Session {self.session_id}>'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'session_id': self.session_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    cart = db.relationship('Cart', back_populates='items')
    product = db.relationship('Product', back_populates='cart_items')

    def __repr__(self):
        return f'<CartItem {self.id} in Cart {self.cart_id}>'

    def serialize(self):
        return {
            'id': self.id,
            'cart_id': self.cart_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', back_populates='orders')
    order_items = db.relationship('OrderItem', back_populates='order', cascade='all, delete-orphan')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'total_amount': self.total_amount,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'order_items': [item.serialize() for item in self.order_items]
        }

class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship('Order', back_populates='order_items')
    product = db.relationship('Product', back_populates='order_items')

    def serialize(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price,
            'product': self.product.serialize() if self.product else None
        }


# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from flask_login import UserMixin
# from datetime import datetime

# metadata = MetaData()
# db = SQLAlchemy(metadata=metadata)

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     reset_token = db.Column(db.String(255), nullable=True)
#     reset_token_expiration = db.Column(db.DateTime, nullable=True)
    
    
    
#     orders = db.relationship('Order', back_populates='user')

#     def __repr__(self):
#         return f'<User {self.username}>'
    
#     def serialize(self):
#         return {
#             'id': self.id,
#             'username': self.username,
#             'email': self.email,
#             'created_at': self.created_at.isoformat(),
#             'reset_token': self.reset_token,
#             'reset_token_expiration': self.reset_token_expiration.isoformat() if self.reset_token_expiration else None
#         }

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     image_url = db.Column(db.String(255), nullable=True)
#     description = db.Column(db.Text, nullable=True)
#     price = db.Column(db.Float, nullable=False)
#     stock = db.Column(db.Integer, nullable=False, default=0)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
#     category = db.relationship('Category', backref=db.backref('products', lazy=True))


#     order_items = db.relationship('OrderItem', back_populates='product')
    
#     def __repr__(self):
#         return f'<Product {self.name}>'
    
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'image_url': self.image_url,
#             'description': self.description,
#             'price': self.price,
#             'stock': self.stock,
#             'created_at': self.created_at.isoformat(),
#             'updated_at': self.updated_at.isoformat(),
#             'category_id': self.category_id
#         }

# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     def __repr__(self):
#         return f'<Category {self.name}>'
    
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'created_at': self.created_at.isoformat(),
#             'updated_at': self.updated_at.isoformat()
#         }

# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable to accommodate non-authenticated users
#     session_id = db.Column(db.String(255), nullable=True)  # New field for session-based carts
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     user = db.relationship('User', backref=db.backref('carts', lazy=True))

#     def __repr__(self):
#         return f'<Cart {self.id} for User {self.user_id} or Session {self.session_id}>'

#     def serialize(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'session_id': self.session_id,
#             'created_at': self.created_at.isoformat(),
#             'updated_at': self.updated_at.isoformat()
#         }

# class CartItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False, default=1)
#     price = db.Column(db.Float, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     cart = db.relationship('Cart', backref=db.backref('items', lazy=True))
#     product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))

#     def __repr__(self):
#         return f'<CartItem {self.id} in Cart {self.cart_id}>'

#     def serialize(self):
#         return {
#             'id': self.id,
#             'cart_id': self.cart_id,
#             'product_id': self.product_id,
#             'quantity': self.quantity,
#             'price': self.price,
#             'created_at': self.created_at.isoformat(),
#             'updated_at': self.updated_at.isoformat()
#         }



# class Order(db.Model):
#     __tablename__ = 'orders'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
#     total_amount = db.Column(db.Float, nullable=False)
#     status = db.Column(db.String(50), nullable=False, default='Pending')
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
#     # Relationship to the User
#     user = db.relationship('User', back_populates='orders')
    
#     # Relationship to OrderItem
#     order_items = db.relationship('OrderItem', back_populates='order', cascade='all, delete-orphan')

#     def __init__(self, user_id, total_amount, status='Pending'):
#         self.user_id = user_id
#         self.total_amount = total_amount
#         self.status = status

#     def serialize(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'total_amount': self.total_amount,
#             'status': self.status,
#             'created_at': self.created_at.isoformat(),
#             'updated_at': self.updated_at.isoformat(),
#             'order_items': [item.serialize() for item in self.order_items]
#         }


# class OrderItem(db.Model):
#     __tablename__ = 'order_items'

#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Float, nullable=False)

#     # Relationship to the Order
#     order = db.relationship('Order', back_populates='order_items')
    
#     # Relationship to the Product
#     product = db.relationship('Product', back_populates='order_items')

#     def __init__(self, order_id, product_id, quantity, price):
#         self.order_id = order_id
#         self.product_id = product_id
#         self.quantity = quantity
#         self.price = price

#     def serialize(self):
#         return {
#             'id': self.id,
#             'order_id': self.order_id,
#             'product_id': self.product_id,
#             'quantity': self.quantity,
#             'price': self.price,
#             'product': self.product.serialize() if self.product else None
#         }
