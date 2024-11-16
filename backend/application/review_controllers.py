from flask import Blueprint, jsonify, request,Flask,send_from_directory, render_template,redirect
from application.models import User, Admin, Reviews
from application.database import db
from flask_restful import Api
from .api import UserBlog, AdminBlogResource,UserReview,AdminReviewResource
import os
from flask_swagger_ui import get_swaggerui_blueprint # Assuming api.py is in the same directory
from datetime import datetime
review_blueprint = Blueprint("review", __name__)

SWAGGER_URL = '/api/review/docs'  # Unique URL for blog docs
API_URL = '/api/review_api.yaml'

# blog_controllers.py
swagger_review_ui_blueprint = get_swaggerui_blueprint(
    '/api/review/docs',  # SWAGGER_URL
    '/api/review_api.yaml',  # API_URL
    config={
        'app_name': "Review API Documentation by Anirudh",
        'title': "Review API Documentation by Anirudh",
        'swagger_ui_config': {
            'docExpansion': 'none',
            'displayRequestDuration': True,
            'operationsSorter': 'alpha',
            'defaultModelsExpandDepth': -1,
            'defaultModelExpandDepth': 3
        }
    },
    blueprint_name='swagger_review'
)

@review_blueprint.route('/review_api.yaml')
def review_serve_admin_swagger():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    response = send_from_directory(current_dir, 'review_api.yaml')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response



api = Api(review_blueprint)

# Add the resources to the API
api.add_resource(UserBlog, '/user_review/<int:id>')
api.add_resource(AdminBlogResource, '/admin_review/<int:id>')


@review_blueprint.route("/getReviewInfo/<int:id>", methods=['GET', 'POST'])
def getReviewInfo(id):
    # Query all data for admin with admin_id=1 and convert to dictionary
    all_data = db.session.execute(db.Select(Reviews).where(Reviews.admin_id == 1)).scalars().all()
    all_data_serialized = [blog.to_dict() for blog in all_data]  # Convert Reviews instances to dict

    # Query blogs for the given user id and convert to dictionary
    blogs = db.session.execute(db.Select(Reviews).where(Reviews.user_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    # Return the data as JSON
    return jsonify({
        'review': all_data_serialized,
        'my_reviews': blogs_serialized
    }), 200


@review_blueprint.route("/getOtherReviewInfo/<int:id>", methods=['GET', 'POST'])
def getOtherReviewInfo(id):
    # Query blogs for the given user id and convert to dictionary
    blogs = db.session.execute(db.Select(Reviews)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    # Return the data as JSON
    return jsonify({
        'other_review': blogs_serialized
    }), 200


@review_blueprint.route("/getAllReviewInfo", methods=['GET', 'POST'])
def getAllReviewInfo():
    # Query all data for admin with admin_id=1 and convert to dictionary
    all_data = db.session.execute(db.Select(Reviews).where(Reviews.admin_id == 1)).scalars().all()
    all_data_serialized = [blog.to_dict() for blog in all_data]  # Convert AdminBlog instances to dict

    # Query blogs for the given user id and convert to dictionary
    blogs = db.session.execute(db.select(Reviews)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    # Return the data as JSON
    return jsonify({
        'review': all_data_serialized,
        'user_review': blogs_serialized
    }), 200


@review_blueprint.route("/getAInfoReview/<int:id>", methods=['GET', 'POST'])
def getAInfoReview(id):
    blogs = db.session.execute(db.Select(Reviews).where(Reviews.admin_blog_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert AdminBlog instances to dict

    return jsonify({
        'review': blogs_serialized[0]
    }), 200


@review_blueprint.route("/getInfoReview/<int:id>", methods=['GET', 'POST'])
def getInfoReview(id):
    blogs = db.session.execute(db.Select(Reviews).where(Reviews.blog_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    return jsonify({
        'review': blogs_serialized
    }), 200


@review_blueprint.route("/getAdminInfoReview/<int:id>", methods=['GET', 'POST'])
def getAdminInfoReview(id):
    blogs = db.session.execute(db.Select(Reviews).where(Reviews.admin_blog_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert AdminBlog instances to dict

    return jsonify({
        'review': blogs_serialized[0]
    }), 200


@review_blueprint.route("/create_review/<int:id>/<int:user_id>", methods=['POST'])
def create_review(id,user_id):
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    rating = data.get("rating")

    # Calling the `post` method from `UserBlog` resource to create a new blog
    user_review = UserReview()
    return user_review.post(id,user_id)


@review_blueprint.route("/edit_review/<int:id>/<int:user_id>", methods=['POST','PUT'])
def edit_review(id,user_id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("description")
    body = data.get("rating")

    # Calling the `put` method from `UserBlog` resource to edit an existing blog
    user_review = UserReview()
    return user_review.put(id,user_id)


@review_blueprint.route("/delete_review/<int:id>/<int:user_id>", methods=['POST','DELETE'])
def delete_review(id,user_id):
    # Calling the `delete` method from `UserBlog` resource to delete an existing blog
    user_review = UserReview()
    return user_review.delete(id,user_id)


@review_blueprint.route("/create_admin_review/<int:id>/<int:admin_id>", methods=['POST'])
def create_admin_review(id,admin_id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("description")
    body = data.get("rating")

    # Calling the `post` method from `AdminBlogResource` to create a new admin blog
    admin_review = AdminReviewResource()
    return admin_review.post(id,admin_id)


@review_blueprint.route("/edit_admin_review/<int:id>/<int:admin_id>", methods=['POST','PUT'])
def edit_admin_review(id,admin_id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("description")
    body = data.get("rating")

    # Calling the `put` method from `AdminBlogResource` to edit an existing admin blog
    admin_review = AdminReviewResource()
    return admin_review.put(id,admin_id)


@review_blueprint.route("/delete_admin_review/<int:id>/<int:admin_id>", methods=['POST','DELETE'])
def delete_admin_review(id,admin_id):
    # Calling the `delete` method from `AdminBlogResource` to delete an existing admin blog
    admin_review = AdminReviewResource()
    return admin_review.delete(id,admin_id)
