from flask_restful import Resource, reqparse
from flask import Response
from models import db,Category
import json

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
