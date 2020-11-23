import os
from PIL import Image
import secrets
from flask import render_template, url_for, flash, redirect, make_response, request
from trial import app, db, bcrypt, mail
#Import Message class from Mail extension
from flask_mail import Message
from flask_login import login_user, current_user, logout_user, login_required
from trial.forms import (DefectReportForm, LeaveForm, LoginForm, BlogPostForm, RegistrationForm, 
                        UpdateAccountForm, RequestResetForm, ResetPasswordForm)
from trial.models import Leave, Rehabilitation, Upgrading, Construction, Regravelling, User
from trial.construc import construc_data, update_construc
from trial.rehab import rehab_data, update_rehab
from trial.regrav import regrav_data, update_regrav
from trial.upgrage import upgrade_data, update_upgrade
import pdfkit




#Create route for home app
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #Hash Password
        hashed_pswd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #Create Instance of the user
        user = User(username=form.username.data, email=form.email.data, password=hashed_pswd)
        #Add user to the database
        db.session.add(user)
        db.session.commit()
        flash('New user has been added successfully. You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #Get User from Database
        user = User.query.filter_by(email=form.email.data).first()
        #Check to see if user can be found then log in user
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #Get the next parameter(if it exists redirect the user the requested page)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Unsuccessful Login. Please check email and password again', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#define a save picture function
#Takes picture data as an argument
def save_picture(form_picture):
    #Randomize the name of the picture(to prevent collision with other image with the same name)
    random_hex = secrets.token_hex(8)
    #Grab the file extension
    _, f_ext = os.path.splitext(form_picture.filename)      #Use of underscore to discard the filename
    #Combine the random_hex eith the file extension to get the new filename of image
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    #Resize the Image submitted
    output_size = (125, 125)
    i = Image.open(form_picture)
    #Resize the Image
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

#route for account template
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        #Check if there is a picture data
        if form.picture.data:
            #Set the user profile picture
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        #Set Updated details in the database
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    #Populate fields with data from the database
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', form=form, image_file=image_file)


#Function to send reset email
def send_reset_email(user):
    token = user.get_reset_token()
    #Create email message
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f''' To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made
'''

    #Send message
    mail.send(msg)

#Route to request reset Password(Where Email is entered to reset password)
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

#Route for Reset Password
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Token is invalid or expired', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        #Hash Password
        hashed_pswd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #Edit the password in the database
        user.password = hashed_pswd
        db.session.commit()
        flash('Password has been updated successfully!. You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form) 


#Route to view the Leave form
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Leave.query.get_or_404(post_id)
    return render_template('render_form.html', post=post)

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
@login_required
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        le_ave = Leave(name=form.name.data, rank=form.rank.data, section=form.section.data, date_app=form.date_app.data,
                    tele_no=form.tele_no.data, leave_cat=form.leave_cat.data, no_of_days=form.no_of_days.data, 
                    start_date=form.start_date.data, end_date=form.end_date.data, supp_info=form.supp_info.data,
                    address=form.address.data, mobile_no=form.mobile_no.data, email=form.email.data, 
                    days_proceed=form.days_proceed.data, effec_date=form.effec_date.data, resump_date=form.resump_date.data,
                    outs_days=form.outs_days.data, author=current_user)
        db.session.add(le_ave)
        db.session.commit()
        flash(f"Leave form submitted successfully", 'success')
        return redirect(url_for('view_form', post_id=le_ave.id))
    return render_template('leave_form.html', title='Leave Form Report', form=form)

@app.route('/table')
def table():
    return render_template('tables.html', title='Basic')

#Route for View form 
@app.route('/view_form/<int:post_id>', methods=['GET', 'POST'])
def view_form(post_id):
    post = Leave.query.get_or_404(post_id)
    return render_template('view_lv_form.html', title='Leave', post=post)

@app.route('/get_pdf/<int:post_id>', methods=['GET','POST'])
def get_pdf(post_id):

    post = Leave.query.get_or_404(post_id)
    rendered= render_template('render_form.html', title=current_user.username, post=post)
    css = ['trial/static/css/bootstrap.min.css', 'trial/static/css/style.css']

    options = {'enable-local-file-access': None}
    pdf = pdfkit.from_string(rendered, False, options=options, css=css)
    response = make_response(pdf)
    
    response.headers['content-Type'] = 'application/pdf'
    response.headers['content-Disposition'] = 'inline; filename=output.pdf'

    return response
    

#Create route for Blog news update
@app.route('/blog_news/new', methods=['GET', 'POST'])
@login_required
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

@app.route('/completed/periodic', methods=['GET'])
def completed_periodic():
    return render_template('completed_periodic.html', title='Completed Periodic Projects')

@app.route('/ongoing/periodic', methods=['GET'])
def ongoing_periodic():
    return render_template('ongoing_periodic.html', title='Ongoing Periodic Projects')

@app.route('/planning/periodic', methods=['GET'])
def planning_periodic():
    return render_template('planning_periodic.html', title='Periodic Projects Under Planning')

@app.route('/const')
def const():
    update_construc(construc_data)
    return redirect(url_for('home'))

@app.route('/regrav')
def regrav():
    update_regrav(regrav_data)
    return redirect(url_for('home'))

@app.route('/rehab')
def rehab():
    update_rehab(rehab_data)
    return redirect(url_for('home'))

@app.route('/upgrade')
def upgrade():
    update_upgrade(upgrade_data)
    return redirect(url_for('home'))

@app.route('/rehabilitation', methods=['GET', 'POST'])
def rehabilitation():
    rehab_list = Rehabilitation.query.all()
    return render_template('rehabilitation.html', title='Rehabilitation', rehab_list=rehab_list)

@app.route('/upgrading', methods=['GET', 'POST'])
def upgrading():
    upgrade_list = Upgrading.query.all()
    return render_template('Upgrading.html', title='Upgrading', upgrade_list=upgrade_list)

@app.route('/construction', methods=['GET', 'POST'])
def construction():
    const_list = Construction.query.all()
    return render_template('construction.html', title='Construction', const_list=const_list)

@app.route('/regravelling', methods=['GET', 'POST'])
def regravelling():
    regrav_list = Regravelling.query.all()
    return render_template('regravelling.html', title='Regravelling', regrav_list=regrav_list)

@app.route('/render/<int:post_id>', methods=['GET', 'POST'])
def render(post_id):
    post = Leave.query.get_or_404(post_id)
    return render_template('render_form.html', post=post, title=current_user.username)