from flask import Blueprint, render_template
from trial.models import Post

errors = Blueprint('errors', __name__)

#Create a Decorator for error handling

@errors.app_errorhandler(404)
def error_404(error):
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('errors/404.html', posts=posts), 404

@errors.app_errorhandler(403)
def error_403(error):
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('errors/403.html', posts=posts), 403

@errors.app_errorhandler(500)
def error_500(error): 
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('errors/500.html', posts=posts), 500
