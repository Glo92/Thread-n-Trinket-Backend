from flask_restful import Resource, reqparse
from flask import request, jsonify
from models import db, Order, OrderItem, Product
from flask_jwt_extended import jwt_required, get_jwt_identity

class OrderResource(Resource):
    @jwt_required()
    def get(self, order_id=None):
        user_id = get_jwt_identity()

        if order_id:
            order = Order.query.filter_by(id=order_id, user_id=user_id).first()
            if order:
                return jsonify(order.serialize())
            return {'message': 'Order not found'}, 404

        orders = Order.query.filter_by(user_id=user_id).all()
        return jsonify([order.serialize() for order in orders])

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.json
        order_items_data = data.get('order_items', [])
        total_amount = 0

        if not order_items_data:
            return {'message': 'No order items provided'}, 400

        order = Order(user_id=user_id, total_amount=0, status='Pending')

        for item_data in order_items_data:
            product = Product.query.get(item_data['product_id'])
            if product:
                quantity = item_data.get('quantity', 1)
                price = product.price * quantity
                total_amount += price
                order_item = OrderItem(order=order, product=product, quantity=quantity, price=price)
                order.order_items.append(order_item)
            else:
                return {'message': f'Product with id {item_data["product_id"]} not found'}, 404

        order.total_amount = total_amount
        db.session.add(order)
        db.session.commit()

        return jsonify(order.serialize()), 201

    @jwt_required()
    def put(self, order_id):
        user_id = get_jwt_identity()
        data = request.json

        order = Order.query.filter_by(id=order_id, user_id=user_id).first()
        if not order:
            return {'message': 'Order not found'}, 404

        status = data.get('status')
        if status:
            order.status = status

        db.session.commit()
        return jsonify(order.serialize()), 200

    @jwt_required()
    def delete(self, order_id):
        user_id = get_jwt_identity()

        order = Order.query.filter_by(id=order_id, user_id=user_id).first()
        if not order:
            return {'message': 'Order not found'}, 404

        db.session.delete(order)
        db.session.commit()
        return {'message': 'Order deleted'}, 200
