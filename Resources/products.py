
from flask_restful import Resource, reqparse
from flask import Response
from models import Product, db,Category
import json


class ProductResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Product name cannot be blank')
        parser.add_argument('image_url')  # Moved image_url right after name
        parser.add_argument('description')
        parser.add_argument('price', type=float, required=True, help='Price cannot be blank')
        parser.add_argument('stock', type=int, required=True, help='Stock cannot be blank')
        parser.add_argument('category_id', type=int, required=True, help='Category ID cannot be blank')
        args = parser.parse_args()

        try:
            product = Product(
                name=args['name'],
                image_url=args.get('image_url'),  # Set image_url right after name
                description=args.get('description'),
                price=args['price'],
                stock=args['stock'],
                category_id=args['category_id']
            )
            db.session.add(product)
            db.session.commit()
            response_data = {'message': 'Product created successfully', 'product_id': product.id}
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=201, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to create product', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class ProductListResource(Resource):
    def get(self):
        try:
            products = Product.query.all()
            response_data = [{
                'id': product.id,
                'name': product.name,
                'image_url': product.image_url,  # Moved image_url right after name
                'description': product.description,
                'price': product.price,
                'stock': product.stock,
                'category_id': product.category_id
            } for product in products]
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=200, mimetype='application/json')
        except Exception as e:
            error_message = {'message': 'Failed to retrieve products', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class ProductUpdateResource(Resource):
    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('image_url')  # Moved image_url right after name
        parser.add_argument('description')
        parser.add_argument('price', type=float)
        parser.add_argument('stock', type=int)
        parser.add_argument('category_id', type=int)
        args = parser.parse_args()

        try:
            product = Product.query.get_or_404(product_id)
            if args['name'] is not None:
                product.name = args['name']
            if args.get('image_url') is not None:
                product.image_url = args['image_url']
            if args['description'] is not None:
                product.description = args['description']
            if args['price'] is not None:
                product.price = args['price']
            if args['stock'] is not None:
                product.stock = args['stock']
            if args.get('category_id') is not None:
                product.category_id = args['category_id']

            db.session.commit()
            response_data = {'message': 'Product updated successfully'}
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=200, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to update product', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class ProductDeleteResource(Resource):
    def delete(self, product_id):
        try:
            product = Product.query.get_or_404(product_id)
            db.session.delete(product)
            db.session.commit()
            response_data = {'message': 'Product deleted successfully'}
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=204, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to delete product', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')


class CategoryResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Category name cannot be blank')
        parser.add_argument('description')
        args = parser.parse_args()

        try:
            category = Category(
                name=args['name'],
                description=args.get('description')
            )
            db.session.add(category)
            db.session.commit()
            response_data = {'message': 'Category created successfully', 'category_id': category.id}
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=201, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to create category', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class CategoryListResource(Resource):
    def get(self):
        try:
            categories = Category.query.all()
            response_data = [{
                'id': category.id,
                'name': category.name,
                'description': category.description
            } for category in categories]
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=200, mimetype='application/json')
        except Exception as e:
            error_message = {'message': 'Failed to retrieve categories', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class CategoryUpdateResource(Resource):
    def put(self, category_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('description')
        args = parser.parse_args()

        try:
            category = Category.query.get_or_404(category_id)
            if args['name'] is not None:
                category.name = args['name']
            if args['description'] is not None:
                category.description = args['description']
            
            db.session.commit()
            response_data = {'message': 'Category updated successfully'}
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=200, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to update category', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class CategoryDeleteResource(Resource):
    def delete(self, category_id):
        try:
            category = Category.query.get_or_404(category_id)
            db.session.delete(category)
            db.session.commit()
            response_data = {'message': 'Category deleted successfully'}
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=204, mimetype='application/json')
        except Exception as e:
            db.session.rollback()
            error_message = {'message': 'Failed to delete category', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')
