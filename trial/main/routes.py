from flask import render_template, Blueprint, g, current_app, redirect, url_for, request
from trial.main.forms import SearchForm
from trial.models import Post, Upgrading


main = Blueprint('main', __name__)

#Create route for home app
@main.route('/')
@main.route('/home')
def home(): 
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/home.html', posts=posts) 

#Create a route for divisions
@main.route('/divisions')
def division():
    posts = Post.query.order_by(Post.id.desc()).all() 
    return render_template('main/divisions.html', title='Division', posts=posts)

#Create a route for basic layout
@main.route('/basic')
def basic():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/basic_temp.html', title='Basic', posts=posts)

@main.route('/road_net')
def road_net():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/road_network.html', title='Basic', posts=posts)

@main.route('/mission')
def mission():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/mission.html', title='Basic', posts=posts)

@main.route('/leaders')
def leaders():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/leadership.html', title='Basic', posts=posts)

@main.route('/contractors')
def contractors():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/contractor_list.html', title='Basic', posts=posts)

@main.route('/organogram')
def organogram():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/organogram.html', title='Organogram', posts=posts)

@main.route('/completed/periodic', methods=['GET', 'POST'])
def completed_periodic():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/completed_periodic.html', title='Completed Periodic Projects', posts=posts)

@main.route('/ongoing/periodic', methods=['GET', 'POST'])
def ongoing_periodic():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/ongoing_periodic.html', title='Ongoing Periodic Projects', posts=posts)

@main.route('/planning/periodic', methods=['GET', 'POST'])
def planning_periodic():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/planning_periodic.html', title='Periodic Projects Under Planning', posts=posts)

@main.before_app_request
def before_request():
    g.search_form = SearchForm()

@main.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.home'))
    page = request.args.get('page', 1, type=int)
    search_posts, total = Upgrading.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/search.html', title='Search', search_posts=search_posts,
                           next_url=next_url, prev_url=prev_url, posts=posts)