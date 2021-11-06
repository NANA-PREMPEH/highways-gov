from flask import render_template, Blueprint, g, current_app, redirect, url_for, request, jsonify, flash
from trial import db, bcrypt
from werkzeug.urls import url_parse
from flask_login import current_user, login_user
from trial.main.forms import SearchForm
from trial.projects.forms import DateForm
from trial.models import CompletedProj, Post, Gallery, User
from trial.users.forms import RequestResetForm, ResetPasswordForm, LoginForm, UpdateAccountForm


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

#Create a route for divisions
@main.route('/no_info')
def no_info():
    posts = Post.query.order_by(Post.id.desc()).all() 
    return render_template('main/no_info.html', title='No Info', posts=posts) 

#Create a route for Landing Page
@main.route('/main/landing_page')
def landing_page():
    
    return render_template('landing/landing_page.html')



#Create a route for Yearly Report 
@main.route('/report/yearly_report/')
def yearly_report():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/yearly_report.html', title='Yearly Report', posts=posts)

#Create a route for 2018 report 
@main.route('/yearly_report/2018')
def report_2018():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/report_2018.html', title='2018 Report', posts=posts)

#Create a route for 2019 report 
@main.route('/yearly_report/2019')
def report_2019():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/report_2019.html', title='2019 Report', posts=posts)

#Create a route for 2020 report 
@main.route('/report/proj_funding')
def proj_funding():
    posts = Post.query.order_by(Post.id.desc()).all() 
    return render_template('main/proj_funding.html', title='2020 Report', posts=posts)

@main.route('/institution_profile')
def inst_prof():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/institution_profile.html', title='Institution Profile', posts=posts)

@main.route('/directors_office')
def directors_office():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/directors_office.html', title='Institution Profile', posts=posts)

@main.route('/road_net')
def road_net():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/road_network.html', title='Road Network', posts=posts)

@main.route('/photo_gallery')
def photo_gallery():
    posts = Post.query.order_by(Post.id.desc()).all()
    pics = Gallery.query.all()
    return render_template('main/photo-gallery.html', title='Gallery', posts=posts, pics=pics)

@main.route('/mission')
def mission():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/mission.html', title='Mission', posts=posts)

@main.route('/leaders')
def leaders():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/leadership.html', title='Leaders', posts=posts)

@main.route('/contractors')
def contractors():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/contractor_list.html', title='Contractor List', posts=posts)

@main.route('/contacts')
def contacts_page():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/contacts_page.html', title='Contractor List', posts=posts)

@main.route('/organogram')
def organogram():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/organogram.html', title='Organogram', posts=posts) 

@main.route('/completed/periodic', methods=['GET', 'POST'])
def completed_periodic():
    
    form = DateForm()
    posts = Post.query.order_by(Post.id.desc()).all() 

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        results = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()
        
        return jsonify({'data': render_template('main/completed_periodic_json.html', results=results, form=form)}) 
        
    return render_template('main/completed_periodic.html', title='Completed Periodic Projects', posts=posts, form=form)

@main.route('/ongoing/periodic', methods=['GET', 'POST'])
def ongoing_periodic():
    
    form = DateForm()
    posts = Post.query.order_by(Post.id.desc()).all() 

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        results = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()
        
        return jsonify({'data': render_template('main/ongoing_periodic_json.html', results=results, form=form)}) 
        
    return render_template('main/ongoing_periodic.html', title='Ongoing Periodic Projects', posts=posts, form=form)

@main.route('/completed/routine', methods=['GET', 'POST'])
def completed_routine():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/completed_routine.html', title='Completed Routine Projects', posts=posts)

@main.route('/ongoing/routine', methods=['GET', 'POST'])
def ongoing_routine():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/ongoing_routine.html', title='Ongoing Periodic Projects', posts=posts)

@main.route('/planning/periodic', methods=['GET', 'POST'])
def planning_periodic():
    form=DateForm()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/planning_periodic.html', title='Periodic Projects Under Planning', posts=posts, form=form)

@main.route('/planning/routine', methods=['GET', 'POST'])
def planning_routine():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/planning_routine.html', title='Routine Projects Under Planning', posts=posts)

# Start of Right to information Page
@main.route('/rti_page')
def rti_page():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/rti_page.html', title='RTI Page', posts=posts)

# RTI available_info 
@main.route('/available_info')
def available_info():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/available_info.html', title='Available to Information Page', posts=posts)

# RTI application
@main.route('/application')
def application():
    return render_template('/main/application.html', title='Application to Access Information')


# RTI exempt
@main.route('/exempt_info')
def exempt_info():
    return render_template('/main/exempt_info.html', title='Exempt Information')


# Start of services route
# Services
@main.route('/lab_test_services')
def lab_test_services():
    return render_template('/main/lab_test_services.html', title='Lab test Services')


@main.before_app_request 
def before_request():
    g.search_form = SearchForm()

@main.route('/search')
def search():
    if not g.search_form.validate(): 
        return redirect(url_for('main.home'))
    page = request.args.get('page', 1, type=int)
    search_posts, total = CompletedProj.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('main/search.html', title='Search', search_posts=search_posts,
                           next_url=next_url, prev_url=prev_url, posts=posts)