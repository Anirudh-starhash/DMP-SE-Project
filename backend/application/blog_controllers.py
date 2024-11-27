from flask import Blueprint, jsonify, request,Flask,send_from_directory, render_template,redirect
from application.models import User, Blog, Admin, AdminBlog
from application.database import db
from flask_restful import Api
from .api import UserBlog, AdminBlogResource
import os
from flask_swagger_ui import get_swaggerui_blueprint # Assuming api.py is in the same directory
from datetime import datetime
blog_blueprint = Blueprint("blog", __name__)

SWAGGER_URL = '/api/blog/docs'  # Unique URL for blog docs
API_URL = '/api/blog_api.yaml'

# blog_controllers.py
swagger_blog_ui_blueprint = get_swaggerui_blueprint(
    '/api/blog/docs',  # SWAGGER_URL
    '/api/blog_api.yaml',  # API_URL
    config={
        'app_name': "Blog API Documentation by Anirudh",
        'title': "Blog API Documentation by Anirudh",
        'swagger_ui_config': {
            'docExpansion': 'none',
            'displayRequestDuration': True,
            'operationsSorter': 'alpha',
            'defaultModelsExpandDepth': -1,
            'defaultModelExpandDepth': 3
        }
    },
    blueprint_name='swagger_blog'
)

@blog_blueprint.route('/blog_api.yaml')
def blog_serve_admin_swagger():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    response = send_from_directory(current_dir, 'blog_api.yaml')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response



api = Api(blog_blueprint)

# Add the resources to the API
api.add_resource(UserBlog, '/user_blog/<int:id>')
api.add_resource(AdminBlogResource, '/admin_blog/<int:id>')


@blog_blueprint.route("/getInfo/<int:id>", methods=['GET', 'POST'])
def getInfo(id):
    # Query all data for admin with admin_id=1 and convert to dictionary
    all_data = db.session.execute(db.Select(AdminBlog).where(AdminBlog.admin_id == 1)).scalars().all()
    all_data_serialized = [blog.to_dict() for blog in all_data]  # Convert AdminBlog instances to dict

    # Query blogs for the given user id and convert to dictionary
    blogs = db.session.execute(db.Select(Blog).where(Blog.user_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    # Return the data as JSON
    return jsonify({
        'blogs': all_data_serialized,
        'my_blogs': blogs_serialized
    }), 200


@blog_blueprint.route("/getOtherInfo/<int:id>", methods=['GET', 'POST'])
def getOtherInfo(id):
    # Query blogs for the given user id and convert to dictionary
    blogs = db.session.execute(db.Select(Blog)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    # Return the data as JSON
    return jsonify({
        'other_blogs': blogs_serialized
    }), 200


@blog_blueprint.route("/getAllInfo", methods=['GET', 'POST'])
def getAllInfo():
    # Query all data for admin with admin_id=1 and convert to dictionary
    all_data = db.session.execute(db.Select(AdminBlog).where(AdminBlog.admin_id == 1)).scalars().all()
    all_data_serialized = [blog.to_dict() for blog in all_data]  # Convert AdminBlog instances to dict

    # Query blogs for the given user id and convert to dictionary
    blogs = db.session.execute(db.select(Blog)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    # Return the data as JSON
    return jsonify({
        'blogs': all_data_serialized,
        'user_blogs': blogs_serialized
    }), 200


@blog_blueprint.route("/getAInfoBlog/<int:id>", methods=['GET', 'POST'])
def getAInfoBlog(id):
    blogs = db.session.execute(db.Select(AdminBlog).where(AdminBlog.admin_blog_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert AdminBlog instances to dict
    
    # print(blogs_serialized)
    if blogs_serialized==[] :
        return jsonify ( {
            'blog' : {}
        }),200
    else :
        return jsonify({
            'blog': blogs_serialized[0]
        }), 200


@blog_blueprint.route("/getInfoBlog/<int:id>", methods=['GET', 'POST'])
def getInfoBlog(id):
    blogs = db.session.execute(db.Select(Blog).where(Blog.blog_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert Blog instances to dict

    return jsonify({
        'blog': blogs_serialized[0]
    }), 200


@blog_blueprint.route("/getAdminInfoBlog/<int:id>", methods=['GET', 'POST'])
def getAdminInfoBlog(id):
    blogs = db.session.execute(db.Select(AdminBlog).where(AdminBlog.admin_blog_id == id)).scalars().all()
    blogs_serialized = [blog.to_dict() for blog in blogs]  # Convert AdminBlog instances to dict

    return jsonify({
        'blog': blogs_serialized[0]
    }), 200


@blog_blueprint.route("/create_blob/<int:id>", methods=['POST'])
def create_blog(id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("subtitle")
    body = data.get("body")

    # Calling the `post` method from `UserBlog` resource to create a new blog
    user_blog = UserBlog()
    return user_blog.post(id)


@blog_blueprint.route("/edit_blob/<int:id>", methods=['POST','PUT'])
def edit_blog(id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("subtitle")
    body = data.get("body")

    # Calling the `put` method from `UserBlog` resource to edit an existing blog
    user_blog = UserBlog()
    return user_blog.put(id)


@blog_blueprint.route("/delete_blob/<int:id>", methods=['POST','DELETE'])
def delete_blob(id):
    # Calling the `delete` method from `UserBlog` resource to delete an existing blog
    user_blog = UserBlog()
    return user_blog.delete(id)


@blog_blueprint.route("/create_admin_blob/<int:id>", methods=['POST'])
def create_admin_blog(id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("subtitle")
    body = data.get("body")

    # Calling the `post` method from `AdminBlogResource` to create a new admin blog
    admin_blog = AdminBlogResource()
    return admin_blog.post(id)


@blog_blueprint.route("/edit_admin_blob/<int:id>", methods=['POST','PUT'])
def edit_admin_blog(id):
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("subtitle")
    body = data.get("body")

    # Calling the `put` method from `AdminBlogResource` to edit an existing admin blog
    admin_blog = AdminBlogResource()
    return admin_blog.put(id)


@blog_blueprint.route("/delete_admin_blob/<int:id>", methods=['POST','DELETE'])
def delete_admin_blob(id):
    # Calling the `delete` method from `AdminBlogResource` to delete an existing admin blog
    admin_blog = AdminBlogResource()
    return admin_blog.delete(id)
