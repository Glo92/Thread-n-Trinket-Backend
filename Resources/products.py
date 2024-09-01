from flask_restful import Resource, reqparse
from flask import Response
from models import Product, db
import json

class ProductResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Product name cannot be blank')
        parser.add_argument('image_url')  
        parser.add_argument('description')
        parser.add_argument('price', type=float, required=True, help='Price cannot be blank')
        parser.add_argument('stock', type=int, required=True, help='Stock cannot be blank')
        parser.add_argument('category_id', type=int, required=True, help='Category ID cannot be blank')
        args = parser.parse_args()

        try:
            product = Product(
                name=args['name'],
                image_url=args.get('image_url'),  
                description=args.get('description'),
                price=args['price'],
                stock=args['stock'],
                category_id=args['category_id']
            )
            db.session.add(product)
            db.session.commit()
            response_data = {'message': 'Product created successfully', 'product': product.serialize()}
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
            response_data = [product.serialize() for product in products]
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=200, mimetype='application/json')
        except Exception as e:
            error_message = {'message': 'Failed to retrieve products', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class ProductDetailResource(Resource):
    def get(self, product_id):
        try:
            product = Product.query.get_or_404(product_id)
            response_data = product.serialize()
            response_json = json.dumps(response_data)
            return Response(response=response_json, status=200, mimetype='application/json')
        except Exception as e:
            error_message = {'message': 'Failed to retrieve product', 'error': str(e)}
            response_json = json.dumps(error_message)
            return Response(response=response_json, status=500, mimetype='application/json')

class ProductUpdateResource(Resource):
    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('image_url')  
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
            response_data = {'message': 'Product updated successfully', 'product': product.serialize()}
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








# from flask_restful import Resource, reqparse
# from flask import Response
# from models import Product, db
# import json


# class ProductResource(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', required=True, help='Product name cannot be blank')
#         parser.add_argument('image_url')  
#         parser.add_argument('description')
#         parser.add_argument('price', type=float, required=True, help='Price cannot be blank')
#         parser.add_argument('stock', type=int, required=True, help='Stock cannot be blank')
#         parser.add_argument('category_id', type=int, required=True, help='Category ID cannot be blank')
#         args = parser.parse_args()

#         try:
#             product = Product(
#                 name=args['name'],
#                 image_url=args.get('image_url'),  
#                 description=args.get('description'),
#                 price=args['price'],
#                 stock=args['stock'],
#                 category_id=args['category_id']
#             )
#             db.session.add(product)
#             db.session.commit()
#             response_data = {'message': 'Product created successfully', 'product_id': product.id}
#             response_json = json.dumps(response_data)
#             return Response(response=response_json, status=201, mimetype='application/json')
#         except Exception as e:
#             db.session.rollback()
#             error_message = {'message': 'Failed to create product', 'error': str(e)}
#             response_json = json.dumps(error_message)
#             return Response(response=response_json, status=500, mimetype='application/json')


# class ProductListResource(Resource):
#     def get(self):
#         try:
#             products = Product.query.all()
#             response_data = [{
#                 'id': product.id,
#                 'name': product.name,
#                 'image_url': product.image_url,  
#                 'description': product.description,
#                 'price': product.price,
#                 'stock': product.stock,
#                 'category_id': product.category_id
#             } for product in products]
#             response_json = json.dumps(response_data)
#             return Response(response=response_json, status=200, mimetype='application/json')
#         except Exception as e:
#             error_message = {'message': 'Failed to retrieve products', 'error': str(e)}
#             response_json = json.dumps(error_message)
#             return Response(response=response_json, status=500, mimetype='application/json')

# class ProductDetailResource(Resource):
#     def get(self, product_id):
#         try:
#             product = Product.query.get_or_404(product_id)
#             response_data = {
#                 'id': product.id,
#                 'name': product.name,
#                 'image_url': product.image_url,
#                 'description': product.description,
#                 'price': product.price,
#                 'stock': product.stock,
#                 'category_id': product.category_id
#             }
#             response_json = json.dumps(response_data)
#             return Response(response=response_json, status=200, mimetype='application/json')
#         except Exception as e:
#             error_message = {'message': 'Failed to retrieve product', 'error': str(e)}
#             response_json = json.dumps(error_message)
#             return Response(response=response_json, status=500, mimetype='application/json')
# class ProductUpdateResource(Resource):
#     def put(self, product_id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name')
#         parser.add_argument('image_url')  
#         parser.add_argument('description')
#         parser.add_argument('price', type=float)
#         parser.add_argument('stock', type=int)
#         parser.add_argument('category_id', type=int)
#         args = parser.parse_args()

#         try:
#             product = Product.query.get_or_404(product_id)
#             if args['name'] is not None:
#                 product.name = args['name']
#             if args.get('image_url') is not None:
#                 product.image_url = args['image_url']
#             if args['description'] is not None:
#                 product.description = args['description']
#             if args['price'] is not None:
#                 product.price = args['price']
#             if args['stock'] is not None:
#                 product.stock = args['stock']
#             if args.get('category_id') is not None:
#                 product.category_id = args['category_id']

#             db.session.commit()
#             response_data = {'message': 'Product updated successfully'}
#             response_json = json.dumps(response_data)
#             return Response(response=response_json, status=200, mimetype='application/json')
#         except Exception as e:
#             db.session.rollback()
#             error_message = {'message': 'Failed to update product', 'error': str(e)}
#             response_json = json.dumps(error_message)
#             return Response(response=response_json, status=500, mimetype='application/json')

# class ProductDeleteResource(Resource):
#     def delete(self, product_id):
#         try:
#             product = Product.query.get_or_404(product_id)
#             db.session.delete(product)
#             db.session.commit()
#             response_data = {'message': 'Product deleted successfully'}
#             response_json = json.dumps(response_data)
#             return Response(response=response_json, status=204, mimetype='application/json')
#         except Exception as e:
#             db.session.rollback()
#             error_message = {'message': 'Failed to delete product', 'error': str(e)}
#             response_json = json.dumps(error_message)
#             return Response(response=response_json, status=500, mimetype='application/json')

