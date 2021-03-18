from flask import render_template, redirect, url_for, flash, request, Blueprint
from werkzeug.urls import url_parse
from flask_login import current_user, logout_user, login_required, login_user
from trial import db, bcrypt 
from trial.users.forms import RequestResetForm, ResetPasswordForm, LoginForm, UpdateAccountForm
from trial.users.utils import send_reset_email, save_picture
from trial.models import User, Post, Leave
from trial.staff_list import update_staff, staff
from trial.leavemgt.forms import LeaveAction

users = Blueprint('users', __name__) 


#Route for Login 
@users.route('/login', methods=['GET', 'POST']) 
def login():
    if current_user.is_authenticated:
        if current_user.role_id==1:
            return redirect(url_for('users.user_dashboard',user_name=current_user.name)) 
        elif current_user.role_id==3:
            return redirect(url_for('leavemgt.leave_dash'))
    form = LoginForm()
    if form.validate_on_submit():
        #Get User from Database
        user = User.query.filter_by(acc_gen_no=form.acc_gen.data).first() or User.query.filter_by(email=form.acc_gen.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data): 
            login_user(user, remember=form.remember.data)
            
            #Get the next parameter(if it exists redirect the user the requested page)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                if current_user.role_id==1:
                    next_page = url_for('users.user_dashboard',user_name=current_user.name)
                elif current_user.role_id==3:
                    next_page = url_for('leavemgt.leave_dash')
            return redirect(next_page)

        else:
            flash('Unsuccessful Login. Please check email and password again', 'danger') 
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('users/login.html', title='Login', form=form, posts=posts) 

#route for account template
@users.route('/account', methods=['GET', 'POST']) 
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
        current_user.acc_gen_no = form.acc_gen.data
        current_user.email = form.email.data
        db.session.commit() 
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    #Populate fields with data from the database
    elif request.method == 'GET':
        form.acc_gen.data = current_user.acc_gen_no
        form.email.data = current_user.email
        form.dob.data = current_user.dob

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('users/account.html', title='Account', form=form, posts=posts)


#Route for logout
@users.route('/logout')
def logout():
    logout_user() 
    return redirect(url_for('users.login'))

@users.route('/add_staff_list')
def add_staff_list():
    update_staff(staff)
    return redirect(url_for('admin.dashboard'))

#Route to request reset Password(Where Email is entered to reset password) 
@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() 
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users.login'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('users/reset_request.html', title='Reset Password', form=form, posts=posts)

#Route for Reset Password
@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token) 
    if user is None:
        flash('Token is invalid or expired', 'warning')
        return redirect(url_for('users.reset_request')) 
    form = ResetPasswordForm()
    if form.validate_on_submit():
        #Hash Password
        hashed_pswd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #Edit the password in the database
        user.password = hashed_pswd
        db.session.commit()
        flash('Password has been updated successfully!. You can now log in', 'success')
        return redirect(url_for('users.login'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('users/reset_token.html', title='Reset Password', form=form, posts=posts)  

#Route to view user dashboard
@users.route('/user_dashboard/<string:user_name>', methods=['GET', 'POST'])
@login_required
def user_dashboard(user_name):
    form = LeaveAction()

    all_req = Leave.query.filter_by(name=user_name)
    total_req = Leave.query.filter_by(name=user_name).count()
    rej_no = Leave.query.filter_by(name=user_name, leave_status="Rejected").count()
    app_no = Leave.query.filter_by(name=user_name, leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(name=user_name, leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(name=user_name, leave_status="Pending").count()

    return render_template('users/user_leave_dash.html', all_req=all_req, form=form,total_req = total_req, 
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no)


@users.route('/decide_on_leave_req/<int:leave_id>', methods=['GET', 'POST'])
@login_required
def act_on_leave_req(leave_id):
    form = LeaveAction()
    req = Leave.query.get_or_404(leave_id)
    if form.validate_on_submit():
        if form.cancel.data:
            req.leave_status = form.cancel.data
        db.session.commit()
    return redirect(url_for('users.user_dashboard',user_name=current_user.name))

#Route to view user's pending requests
@users.route('/user_leave_request/<string:username>/pending_requests', methods=['GET', 'POST'])
def user_pending_req(username):
    form = LeaveAction()
    pending = Leave.query.filter_by(name=username)
    total_req = Leave.query.filter_by(name=username).count()
    rej_no = Leave.query.filter_by(name=username, leave_status="Rejected").count()
    app_no = Leave.query.filter_by(name=username, leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(name=username, leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(name=username, leave_status="Pending").count()
    return render_template('users/user_pending.html', form=form, pending=pending,total_req = total_req,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no,
                            title="Pending Requests")

#Route to view user's rejected requests
@users.route('/user_leave_request/<string:username>/rejected_requests', methods=['GET', 'POST'])
def user_rejected_req(username):
    form = LeaveAction()
    rejected = Leave.query.filter_by(name=username)
    total_req = Leave.query.filter_by(name=username).count()
    rej_no = Leave.query.filter_by(name=username, leave_status="Rejected").count()
    app_no = Leave.query.filter_by(name=username, leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(name=username, leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(name=username, leave_status="Pending").count()
    return render_template('users/user_rejected.html', form=form, rejected=rejected, total_req = total_req,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no, 
                            title="Rejected Requests")

#Route to view user's cancelled requests
@users.route('/user_leave_request/<string:username>/cancelled_requests', methods=['GET', 'POST'])
def user_cancelled_req(username):
    form = LeaveAction()
    cancelled = Leave.query.filter_by(name=username)
    total_req = Leave.query.filter_by(name=username).count()
    rej_no = Leave.query.filter_by(name=username, leave_status="Rejected").count()
    app_no = Leave.query.filter_by(name=username, leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(name=username, leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(name=username, leave_status="Pending").count()
    return render_template('users/user_cancelled.html', form=form, cancelled=cancelled, total_req = total_req,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no,
                            title="Cancelled Requests")

#Route to view user's approved requests
@users.route('/user_leave_request/<string:username>/approved_requests', methods=['GET', 'POST'])
def user_approved_req(username):
    form = LeaveAction()
    approved = Leave.query.filter_by(name=username)
    total_req = Leave.query.filter_by(name=username).count()
    rej_no = Leave.query.filter_by(name=username, leave_status="Rejected").count()
    app_no = Leave.query.filter_by(name=username, leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(name=username, leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(name=username, leave_status="Pending").count()
    return render_template('users/user_approved.html', form=form, approved=approved, total_req = total_req,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no,
                            title="Approved Requests")


