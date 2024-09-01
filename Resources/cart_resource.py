from flask_restful import Resource, reqparse
from flask import Response, request
from models import db, Cart, CartItem, Product
import json

class AddToCartResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session_id', type=str, required=True, help='Session ID is required')
        parser.add_argument('product_id', type=int, required=True, help='Product ID is required')
        parser.add_argument('quantity', type=int, default=1, help='Quantity of the product')
        args = parser.parse_args()

        try:
            cart = Cart.query.filter_by(session_id=args['session_id']).first()
            if not cart:
                cart = Cart(user_id=None, session_id=args['session_id'])
                db.session.add(cart)
                db.session.commit()


            cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=args['product_id']).first()
            if cart_item:
                cart_item.quantity += args['quantity']
                cart_item.price = Product.query.get(args['product_id']).price
            else:
                product = Product.query.get(args['product_id'])
                if not product:
                    return Response(response=json.dumps({'message': 'Product not found'}), status=404, mimetype='application/json')
                cart_item = CartItem(
                    cart_id=cart.id,
                    product_id=args['product_id'],
                    quantity=args['quantity'],
                    price=product.price
                )
                db.session.add(cart_item)

            db.session.commit()
            return Response(response=json.dumps({'message': 'Item added to cart successfully'}), status=201, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to add item to cart', 'error': str(e)}
            return Response(response=json.dumps(error_message), status=500, mimetype='application/json')

class ViewCartResource(Resource):
    def get(self):
        session_id = request.args.get('session_id')
        try:
            cart = Cart.query.filter_by(session_id=session_id).first_or_404()
            cart_items = CartItem.query.filter_by(cart_id=cart.id).all()
            response_data = {
                'cart_id': cart.id,
                'session_id': cart.session_id,
                'items': [item.serialize() for item in cart_items]
            }
            return Response(response=json.dumps(response_data), status=200, mimetype='application/json')
        except Exception as e:
            error_message = {'message': 'Failed to retrieve cart', 'error': str(e)}
            return Response(response=json.dumps(error_message), status=500, mimetype='application/json')

class UpdateCartResource(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session_id', type=str, required=True, help='Session ID is required')
        parser.add_argument('product_id', type=int, required=True, help='Product ID is required')
        parser.add_argument('quantity', type=int, required=True, help='Quantity of the product')
        args = parser.parse_args()

        try:
            cart = Cart.query.filter_by(session_id=args['session_id']).first_or_404()
            cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=args['product_id']).first_or_404()
            cart_item.quantity = args['quantity']
            cart_item.price = Product.query.get(args['product_id']).price
            db.session.commit()
            return Response(response=json.dumps({'message': 'Cart updated successfully'}), status=200, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to update cart', 'error': str(e)}
            return Response(response=json.dumps(error_message), status=500, mimetype='application/json')

class RemoveFromCartResource(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session_id', type=str, required=True, help='Session ID is required')
        parser.add_argument('product_id', type=int, required=True, help='Product ID is required')
        args = parser.parse_args()

        try:
            cart = Cart.query.filter_by(session_id=args['session_id']).first_or_404()
            cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=args['product_id']).first_or_404()
            db.session.delete(cart_item)
            db.session.commit()
            return Response(response=json.dumps({'message': 'Item removed from cart successfully'}), status=204, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to remove item from cart', 'error': str(e)}
            return Response(response=json.dumps(error_message), status=500, mimetype='application/json')

