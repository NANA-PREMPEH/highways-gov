from flask import render_template, url_for, flash, redirect
from trial.forms import DefectReportForm, LeaveForm, LoginForm, BlogPostForm
from trial.models import Leave
from trial import app, db



#Create route for home app
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "santana" and form.password.data == "password":
            return redirect(url_for('home'))
        else:
            flash(f'Unsuccessful Login. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#Route for Latest news Page
@app.route('/blog')
def blog():
    return render_template('blog.html', title='Latest News')

#Create a route for divisions
@app.route('/divisions')
def division():
    return render_template('divisions.html', title='Division')

#Create a route for basic layout
@app.route('/basic')
def basic():
    return render_template('basic_temp.html', title='Basic')

#Create a route for defect form
@app.route('/defect', methods=['GET', 'POST'])
def defect():
    form = DefectReportForm()
    if form.validate_on_submit():
        flash(f'Defect Report Form submitted successfully', 'success') 
        return redirect(url_for('defect'))
    return render_template('defect_rep.html', title='Road Defects Report', form=form)


#Create a route for just form layout    
@app.route('/leave', methods=['GET', 'POST'])
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        le_ave = Leave(name=form.name.data, rank=form.rank.data, section=form.section.data, date_app=form.date_app.data,
                    tele_no=form.tele_no.data, leave_cat=form.leave_cat.data, no_of_days=form.no_of_days.data, 
                    start_date=form.start_date.data, end_date=form.end_date.data, supp_info=form.supp_info.data,
                    address=form.address.data, mobile_no=form.mobile_no.data, email=form.email.data, 
                    days_proceed=form.days_proceed.data, effec_date=form.effec_date.data, resump_date=form.resump_date.data,
                    outs_days=form.outs_days.data)
        db.session.add(le_ave)
        db.session.commit()
        flash(f"Leave form submitted successfully", 'success')
        return redirect(url_for('view_form'))
    return render_template('leave_form.html', title='Leave Form Report', form=form)

@app.route('/table')
def table():
    return render_template('tables.html', title='Basic')

#Route for View form 
@app.route('/view_form')
def view_form():
    data = Leave.query.all()
    return render_template('view_lv_form.html', title='Leave', data=data)


#Create route for Blog news update
@app.route('/blog_news/new', methods=['GET', 'POST'])
def blog_news():
    form = BlogPostForm()
    return render_template('create_news.html', title='New Post', form=form)

@app.route('/road_net')
def road_net():
    return render_template('road_network.html', title='Basic')

@app.route('/mission')
def mission():
    return render_template('mission.html', title='Basic')

@app.route('/leaders')
def leaders():
    return render_template('leadership.html', title='Basic')

@app.route('/contractors')
def contractors():
    return render_template('contractor_list.html', title='Basic')

@app.route('/organogram')
def organogram():
    return render_template('organogram.html', title='Organogram')