from flask import render_template, Blueprint
from trial.models import Post

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

