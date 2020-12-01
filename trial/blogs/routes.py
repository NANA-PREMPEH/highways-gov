from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import current_user, login_required
from trial import db
from trial.models import Post, Comment
from trial.blogs.forms import BlogPostForm
from trial.blogs.utils import save_photo

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

#Create route for Blog news update
@blogs.route('/blog_news/new', methods=['GET', 'POST'])
@login_required
def blog_news():
    form = BlogPostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.blog_content.data
        picture = save_photo(form.picture.data) 

        #Upload post into the database
        post = Post(title=title, body=content, image=picture, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Post has been submitted', 'success')
        return redirect(url_for('blogs.blog'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('blogs/create_news.html', title='New Post', form=form, posts=posts)

