from flask import render_template, url_for, flash, redirect, request
from trial.forms import DefectForm, LeaveForm, justForm
from trial.models import Leave
from trial import app, db

#Create route for home app
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Latest News')

#Create a route for divisions
@app.route('/divisions')
def division():
    return render_template('divisions.html', title='Division')

#Create a route for divisions
@app.route('/basic')
def basic():
    return render_template('basic_temp.html', title='Basic')

#Create a route for divisions
@app.route('/defect')
def defect():
    form = DefectForm()
    return render_template('defect.html', title='Road Defects Report', form=form)

    
@app.route('/just', methods=['GET', 'POST'])
def just():
    form = justForm()
    if form.validate_on_submit():
        leave = Leave(name=form.name.data, rank=form.rank.data, section=form.section.data, date_app=form.date_app.data,
                    tele_no=form.tele_no.data, leave_cat=form.leave_cat.data, no_of_days=form.no_of_days.data, 
                    start_date=form.start_date.data, end_date=form.end_date.data, supp_info=form.supp_info.data,
                    address=form.address.data, mobile_no=form.mobile_no.data, email=form.email.data, 
                    days_proceed=form.days_proceed.data, effec_date=form.effec_date.data, resump_date=form.resump_date.data,
                    outs_days=form.outs_days.data)
        db.session.add(leave)
        db.session.commit()
        flash(f"Leave form submitted successfully", 'success')
        return redirect(url_for('just'))
    return render_template('just.html', form=form)



#Create a route for leave
@app.route('/leave', methods=['GET', 'POST'])
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        return render_template('home.html')
    return render_template('leave_form.html', title='Leave Form Report', form=form)