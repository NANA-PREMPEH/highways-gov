from flask import render_template, redirect, request, Blueprint
from trial import db
from trial.models import Post, Comment

blogs = Blueprint('blogs', __name__)
 
#Route for Latest news Page
@blogs.route('/blog')
def blog():
    #Get the page you want from a query parameter
    page = request.args.get('page', 1, type=int)
    posts_pag = Post.query.order_by(Post.id.desc()).paginate(page=page, per_page=4)
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('blogs/blog.html', title='Latest News', posts=posts, posts_pag=posts_pag)

#Route for Latest news Page
@blogs.route('/blog_post/<int:post_id>/<string:slug>', methods=['GET', 'POST'])
def blog_post(post_id, slug):
    
    single_post = Post.query.get_or_404(post_id)
    posts = Post.query.order_by(Post.id.desc()).all()
    comments = Comment.query.filter_by(post_id=single_post.id).all()
    if request.method == 'GET':
        single_post.views += 1
        db.session.commit()

    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        comment = Comment(name=name, email=email, message=message, post_id=single_post.id) 
        db.session.add(comment)
        single_post.comments += 1
        
        db.session.commit()
        return redirect(request.url)

    return render_template('blogs/blog_post.html', title='Latest News', single_post=single_post, posts=posts, comments=comments)



