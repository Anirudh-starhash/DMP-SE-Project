from flask import Flask, jsonify, request
from flask_restful import Api, Resource, fields, marshal_with
from application.models import Blog, AdminBlog,Reviews
from application.database import db

app = Flask(__name__)
api = Api(app)

blog_fields = {
    'blog_id': fields.Integer,
    'user_id': fields.Integer,
    'blog_name': fields.String,
    'blog_subtitle': fields.String,
    'blog_content': fields.String
}

admin_blog_fields = {
    'admin_blog_id': fields.Integer,
    'admin_id': fields.Integer,
    'admin_blog_name': fields.String,
    'admin_blog_subtitle': fields.String,
    'admin_blog_content': fields.String
}
review_fields = {
    'blog_id': fields.Integer,
    'user_id': fields.Integer,
    'review_name':fields.String,
    'description': fields.String,
    'rating': fields.Integer,
}
admin_review_fields = {
    'admin_blog_id': fields.Integer,
    'admin_id': fields.Integer,
    'review_name':fields.String,
    'description': fields.String,
    'rating': fields.Integer,
}


class UserBlog(Resource):
    @marshal_with(blog_fields)
    def get(self, id):
        blog = Blog.query.filter_by(blog_id=id).first()
        if blog:
            return blog, 200
        return {'message': 'Blog not found'}, 404

    def post(self, id):
        data = request.get_json()
        title = data.get('title')
        existing_blog = Blog.query.filter_by(blog_name=title).first()
        if existing_blog:
            return {'message': 'Blog already exists'}, 409
        new_blog = Blog(user_id=id, blog_name=title, blog_subtitle=data.get('subtitle'), blog_content=data.get('body'))
        db.session.add(new_blog)
        db.session.commit()
        return {'message': 'Blog created successfully'}, 200

    def put(self, id):
        data = request.get_json()
        blog = Blog.query.filter_by(blog_id=id).first()
        if blog:
            blog.blog_name = data.get('title')
            blog.blog_subtitle = data.get('subtitle')
            blog.blog_content = data.get('body')
            db.session.commit()
            return {'msg': 'Blog updated successfully'}, 200
        return {'msg': 'Blog not found'}, 404

    def delete(self, id):
        blog = Blog.query.filter_by(blog_id=id).first()
        if blog:
            db.session.delete(blog)
            db.session.commit()
            return {'msg': 'Blog deleted successfully'}, 200
        return {'msg': 'Blog not found'}, 404


class AdminBlogResource(Resource):
    @marshal_with(admin_blog_fields)
    def get(self, id):
        blog = AdminBlog.query.filter_by(admin_blog_id=id).first()
        if blog:
            return blog, 200
        return {'msg': 'Admin Blog not found'}, 404

    def post(self, id):
        data = request.get_json()
        title = data.get('title')
        existing_blog = AdminBlog.query.filter_by(admin_blog_name=title).first()
        if existing_blog:
            return {'msg': 'Admin Blog already exists'}, 409
        new_admin_blog = AdminBlog(admin_id=id, admin_blog_name=title, admin_blog_subtitle=data.get('subtitle'), admin_blog_content=data.get('body'))
        db.session.add(new_admin_blog)
        db.session.commit()
        return {'msg': 'Admin Blog created successfully'}, 200

    def put(self, id):
        data = request.get_json()
        blog = AdminBlog.query.filter_by(admin_blog_id=id).first()
        if blog:
            blog.admin_blog_name = data.get('title')
            blog.admin_blog_subtitle = data.get('subtitle')
            blog.admin_blog_content = data.get('body')
            db.session.commit()
            return {'msg': 'Admin Blog updated successfully'}, 200
        return {'msg': 'Admin Blog not found'}, 404

    def delete(self, id):
        blog = AdminBlog.query.filter_by(admin_blog_id=id).first()
        if blog:
            db.session.delete(blog)
            db.session.commit()
            return {'msg': 'Admin Blog deleted successfully'}, 200
        return {'msg': 'Admin Blog not found'}, 404
    
class UserReview(Resource):
    @marshal_with(review_fields)
    def get(self, id):
        review = Reviews.query.filter_by(blog_id=id).first()
        if review:
            return review, 200
        return {'msg': 'Blog not found'}, 404

    def post(self, id,user_id):
        data = request.get_json()
        title = data.get('title')
        existing_review = Reviews.query.filter_by(review_name=title).first()
        if existing_review:
            return {'msg': 'Review already exists'}, 409
        new_review = Reviews(user_id=user_id,blog_id=id, review_name=title, description=data.get('description'), rating=data.get('rating'))
        db.session.add(new_review)
        db.session.commit()
        return {'msg': 'Review created successfully'}, 200

    def put(self, id,user_id):
        data = request.get_json()
        review = Reviews.query.filter_by(blog_id=id).filter_by(user_id=user_id).first()
        if review:
            review.review_name = data.get('title')
            review.description = data.get('description')
            review.rating = data.get('rating')
            db.session.commit()
            return {'msg': 'Review updated successfully'}, 200
        return {'msg': 'Review not found'}, 404

    def delete(self, id,user_id):
        review = Reviews.query.filter_by(blog_id=id).filter_by(user_id=user_id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            return {'msg': 'Review deleted successfully'}, 200
        return {'msg': 'Review not found'}, 404


class AdminReviewResource(Resource):
    @marshal_with(admin_review_fields)
    def get(self, id):
        admin_review = Reviews.query.filter_by(admin_blog_id=id).first()
        if admin_review:
            return admin_review, 200
        return {'msg': 'Admin Review not found'}, 404

    def post(self, id,admin_id):
        data = request.get_json()
        title = data.get('title')
        existing_review = Reviews.query.filter_by(review_name=title).first()
        if existing_review:
            return {'message': 'Admin Review already exists'}, 409
        new_admin_reviews = Reviews(admin_blog_id=id,admin_id=admin_id, review_name=title, description=data.get('description'),rating=data.get('rating'))
        db.session.add(new_admin_reviews)
        db.session.commit()
        return {'msg': 'Admin Review created successfully'}, 200

    def put(self, id,admin_id):
        data = request.get_json()
        review = Reviews.query.filter_by(admin_blog_id=id).filter_by(admin_id=admin_id).first()
        if review:
            review.review_name = data.get('title')
            review.description = data.get('description')
            review.rating = data.get('rating')
            db.session.commit()
            return {'message': 'Admin Review updated successfully'}, 200
        return {'message': 'Admin Review not found'}, 404

    def delete(self, id,admin_id):
        review = Reviews.query.filter_by(admin_blog_id=id).filter(admin_id=admin_id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            return {'message': 'Admin Review deleted successfully'}, 200
        return {'message': 'Admin Review not found'}, 404


api.add_resource(UserBlog, '/user_blog/<int:id>')
api.add_resource(AdminBlogResource, '/admin_blog/<int:id>')
api.add_resource(UserReview, '/user_review/<int:id>')
api.add_resource(AdminReviewResource, '/admin_review/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
