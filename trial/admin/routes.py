import secrets
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import current_user, logout_user, login_required
from trial.models import CompletedProj, Post, OngoingProj, User, TerminatedProj, AwardedProj, PlannedProj
from trial.admin.forms import (RegistrationForm, BlogPostForm, CompletedProjectsForm, UpdateStaffForm, OngoingProjectsForm, 
                                PlannedProjectsForm,TerminatedProjectsForm, AwardedProjectsForm)
from trial.admin.utils import save_photo, save_picture, save_proj_image
import re
import requests
from trial import db, bcrypt 
from trial.users.utils import admin_required


admin = Blueprint('admin', __name__) 



@admin.route('/dashboard')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')


@admin.route('/register', methods=['GET', 'POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #Hash Password
        hashed_pswd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #Create Instance of the user
        user = User(ref_no=form.ref_no.data, acc_gen_no=form.acc_gen.data, ssf_no=form.ssf.data, name=form.name.data, dob=form.dob.data,
                    sex=form.sex.data, job_pos=form.job_pos.data, date_engaged=form.date_engaged.data,
                    pres_appt=form.pres_appt.data, station=form.division.data, email=form.email.data, password=hashed_pswd)
        #Add user to the database
        db.session.add(user)
        db.session.commit()
        flash('New user has been added successfully. You can now log in', 'success')
        return redirect(url_for('admin.register'))
    return render_template('admin/register.html', title='Register', form=form) 

#Create route for Blog news update
@admin.route('/blog_news/new', methods=['GET', 'POST'])
@login_required
@admin_required
def create_blog():
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
    return render_template('admin/create_news.html', title='New Post', form=form)

#Add new Contract details to the database(Completed)
@admin.route('/completed/add_contract', methods=['GET', 'POST'])
@login_required
@admin_required
def add_contract():

    form = CompletedProjectsForm()

    if form.validate_on_submit():
    
        if form.video_link.data:
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = None
            video_thumb = "N/A"
        #Check for Picture Input
        if form.pic_one.data:
            pic_one = save_proj_image(form.pic_one.data)
        else:
            pic_one = "N/A"
        if form.pic_two.data:
            pic_two = save_proj_image(form.pic_two.data)
        else:
            pic_two = "N/A"
        
        category = request.form.get('completed_periodic') or 'N/A' 
        length = form.length.data or 'N/A'
        date_completed = form.date_completed.data or None
        date_commenced = form.date_commenced.data or None
        contract_sum = form.contract_sum.data or None
        amt_to_date = form.amt_to_date.data or None
        video_description = form.video_description.data or "N/A"
        video_title = form.video_title.data or "N/A"

        uploaded_details = CompletedProj(region=form.region.data, project=form.project.data, length=length, 
                                            contractor=form.contractor.data, category=category, date_commenced=date_commenced, 
                                            date_completed=date_completed, contract_sum=contract_sum,
                                            amt_to_date=amt_to_date,video_title=video_title,
                                            video_link=video_link,video_description=video_description,
                                            video_thumb=video_thumb, image_one=pic_one, image_two=pic_two, user_id=current_user.id)
        # saving to database
        db.session.add(uploaded_details)
        db.session.commit()
        flash('Data added successfully', 'success')
        return redirect(url_for('admin.add_contract'))

    return render_template('admin/completed_proj-form.html', form=form)


#Add new Contract details to the database(Terminated)
@admin.route('/terminated_proj/add_contract', methods=['GET', 'POST'])
@login_required
@admin_required
def add_terminated_contract():

    form = TerminatedProjectsForm()

    if form.validate_on_submit():

        if form.video_link.data:
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = None
            video_thumb = "N/A"
        
        category = request.form.get('terminated_proj') or 'N/A'
        revised_date = form.revised_date.data or None
        length = form.length.data or 'N/A'
        date_completed = form.date_completed.data or None
        date_commenced = form.date_commenced.data or None
        revised_sum = form.revised_sum.data or None
        contract_sum = form.contract_sum.data or None
        amt_to_date = form.amt_to_date.data or None
        video_description = form.video_description.data or "N/A"
        video_title = form.video_title.data or "N/A"
        
        uploaded_details = TerminatedProj(region=form.region.data, project=form.project.data, length=length, 
                                            contractor=form.contractor.data, category=category, date_commenced=date_commenced, 
                                            date_completed=date_completed, revised_date=revised_date, contract_sum=contract_sum,
                                            revised_sum=revised_sum,amt_to_date=amt_to_date,video_title=video_title,
                                            video_link=video_link,video_description=video_description,
                                            video_thumb=video_thumb, user_id=current_user.id)        
        # saving to database
        db.session.add(uploaded_details)
        db.session.commit()
        flash('Data added successfully', 'success')
        return redirect(url_for('admin.add_terminated_contract'))

    return render_template('admin/terminated_proj-form.html', form=form)


#Add new Contract details to the database(Terminated)
@admin.route('/awarded_proj/add_contract', methods=['GET', 'POST'])
@login_required
@admin_required
def add_awarded_contract():

    form = AwardedProjectsForm()

    if form.validate_on_submit():

        if form.video_link.data:
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = None
            video_thumb = "N/A"
        
        category = request.form.get('awarded_proj') or 'N/A'
        revised_date = form.revised_date.data or None
        length = form.length.data or 'N/A'
        date_completed = form.date_completed.data or None
        date_commenced = form.date_commenced.data or None
        revised_sum = form.revised_sum.data or None
        contract_sum = form.contract_sum.data or None
        amt_to_date = form.amt_to_date.data or None
        cost_to_complete = form.cost_to_complete.data or None
        video_description = form.video_description.data or "N/A"
        video_title = form.video_title.data or "N/A"
        
        uploaded_details = AwardedProj(region=form.region.data, project=form.project.data, length=length, 
                                            contractor=form.contractor.data, category=category, date_commenced=date_commenced, 
                                            date_completed=date_completed, revised_date=revised_date, contract_sum=contract_sum,
                                            revised_sum=revised_sum,amt_to_date=amt_to_date,cost_to_complete=cost_to_complete,
                                            video_title=video_title,video_link=video_link,video_description=video_description,
                                            video_thumb=video_thumb, user_id=current_user.id)        
        # saving to database
        db.session.add(uploaded_details)
        db.session.commit()
        flash('Data added successfully', 'success')
        return redirect(url_for('admin.add_awarded_contract'))

    return render_template('admin/awarded_proj-form.html', form=form)

#Add new Contract details to the database(Planned)
@admin.route('/planned_proj/add_contract', methods=['GET', 'POST'])
@login_required
@admin_required
def add_planned_contract():

    form = PlannedProjectsForm()

    if form.validate_on_submit():

        if form.video_link.data:
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = None
            video_thumb = "N/A"
        
        category = request.form.get('planned_proj') or 'N/A'
        revised_date = form.revised_date.data or None
        length = form.length.data or 'N/A'
        date_completed = form.date_completed.data or None
        date_commenced = form.date_commenced.data or None
        revised_sum = form.revised_sum.data or None
        contract_sum = form.contract_sum.data or None
        amt_to_date = form.amt_to_date.data or None
        
        video_description = form.video_description.data or "N/A"
        video_title = form.video_title.data or "N/A"
        
        uploaded_details = PlannedProj(region=form.region.data, project=form.project.data, length=length, 
                                            contractor=form.contractor.data, category=category, date_commenced=date_commenced, 
                                            date_completed=date_completed, revised_date=revised_date, contract_sum=contract_sum,
                                            revised_sum=revised_sum,amt_to_date=amt_to_date,video_title=video_title,
                                            video_link=video_link,video_description=video_description,
                                            video_thumb=video_thumb, user_id=current_user.id)        
        # saving to database
        db.session.add(uploaded_details)
        db.session.commit()
        flash('Data added successfully', 'success')
        return redirect(url_for('admin.add_planned_contract'))

    return render_template('admin/planned_proj-form.html', form=form)


#Add new Contract details to the database(Ongoing)
@admin.route('/ongoing/add_contract', methods=['GET', 'POST'])
@login_required
@admin_required
def add_ongoing_contract():

    form = OngoingProjectsForm()

    if form.validate_on_submit():

        if form.video_link.data:
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = None
            video_thumb = "N/A"
        
        category = request.form.get('ongoing_periodic') or 'N/A'
        revised_date = form.revised_date.data or None
        length = form.length.data or 'N/A'
        date_completed = form.date_completed.data or None
        date_commenced = form.date_commenced.data or None
        revised_sum = form.revised_sum.data or None
        contract_sum = form.contract_sum.data or None
        amt_to_date = form.amt_to_date.data or None
        video_description = form.video_description.data or "N/A"
        video_title = form.video_title.data or "N/A"
        
        uploaded_details = OngoingProj(region=form.region.data, project=form.project.data, length=length, 
                                            contractor=form.contractor.data, category=category, date_commenced=date_commenced, 
                                            date_completed=date_completed, revised_date=revised_date, contract_sum=contract_sum,
                                            revised_sum=revised_sum,amt_to_date=amt_to_date,video_title=video_title,
                                            video_link=video_link,video_description=video_description,
                                            video_thumb=video_thumb, user_id=current_user.id)        
        # saving to database
        db.session.add(uploaded_details)
        db.session.commit()
        flash('Data added successfully', 'success')
        return redirect(url_for('admin.add_ongoing_contract'))

    return render_template('admin/ongoing_proj-form.html', form=form)


#Route for logout
@admin.route('/admin_logout')
def admin_logout():
    logout_user()
    return redirect(url_for('users.login'))


#Add new Contract details to the database(Ongoing)
@admin.route('/contract/ongoing/edit/<int:contract_id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_ongoing_contract(contract_id):

    form = OngoingProjectsForm()

    contract = OngoingProj.query.get_or_404(contract_id)

    if form.validate_on_submit():

        if form.video_link.data and form.video_link.data != "N/A":
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = "N/A"
            video_thumb = "N/A"

        contract.region = form.region.data or "N/A"
        contract.project = form.project.data or "N/A"
        contract.contractor = form.contractor.data or "N/A"
        contract.category = form.category.data or 'N/A'
        contract.revised_date = form.revised_date.data or None
        contract.length = form.length.data or 'N/A'
        contract.date_completed = form.date_completed.data or None
        contract.date_commenced = form.date_commenced.data or None
        contract.revised_sum = form.revised_sum.data or None
        contract.contract_sum = form.contract_sum.data or None
        contract.amt_to_date = form.amt_to_date.data or None
        contract.video_description = form.video_description.data or "N/A"
        contract.video_title = form.video_title.data or "N/A"
        contract.video_link = video_link
        contract.video_thumb = video_thumb
        
               
        # saving to database
        db.session.commit()
        flash('Project Updated successfully', 'success')
        return redirect(url_for('admin.ongoing_proj_list'))

    elif request.method == "GET":
        
        form.region.data = contract.region
        form.project.data = contract.project
        form.contractor.data = contract.contractor
        form.category.data = contract.category
        form.revised_date.data = contract.revised_date
        form.length.data = contract.length
        form.date_completed.data = contract.date_completed
        form.date_commenced.data = contract.date_commenced
        form.revised_sum.data = contract.revised_sum
        form.contract_sum.data = contract.contract_sum
        form.amt_to_date.data = contract.amt_to_date
        form.video_description.data =  contract.video_description
        form.video_title.data = contract.video_title
        form.video_link.data = contract.video_link


    return render_template('admin/ongoing_proj-edit.html', form=form, contract=contract, contract_id=contract_id)


#Add new Contract details to the database(Completed)
@admin.route('/contract/completed/edit/<int:contract_id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_completed_contract(contract_id):

    form = CompletedProjectsForm()
    contract = CompletedProj.query.get_or_404(contract_id)
    if form.validate_on_submit():

        if form.video_link.data and form.video_link.data != "N/A":
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = "N/A"
            video_thumb = "N/A"

        contract.region = form.region.data or "N/A"
        contract.project = form.project.data or "N/A"
        contract.contractor = form.contractor.data or "N/A"
        contract.category = form.category.data or 'N/A'
        contract.length = form.length.data or 'N/A'
        contract.date_completed = form.date_completed.data or None
        contract.date_commenced = form.date_commenced.data or None
        contract.contract_sum = form.contract_sum.data or None
        contract.amt_to_date = form.amt_to_date.data or None
        contract.video_description = form.video_description.data or "N/A"
        contract.video_title = form.video_title.data or "N/A"
        contract.video_link = video_link
        contract.video_thumb = video_thumb
        
               
        # saving to database
        db.session.commit()
        flash('Project Updated successfully', 'success')
        return redirect(url_for('admin.completed_proj_list'))

    elif request.method == "GET":
        
        form.region.data = contract.region
        form.project.data = contract.project
        form.contractor.data = contract.contractor
        form.category.data = contract.category
        form.length.data = contract.length
        form.date_completed.data = contract.date_completed
        form.date_commenced.data = contract.date_commenced
        form.contract_sum.data = contract.contract_sum
        form.amt_to_date.data = contract.amt_to_date
        form.video_description.data =  contract.video_description
        form.video_title.data = contract.video_title
        form.video_link.data = contract.video_link


    return render_template('admin/completed_proj-edit.html', form=form, contract=contract, contract_id=contract_id)


#Add new Contract details to the database(Planned)
@admin.route('/contract/planned/edit/<int:contract_id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_planned_contract(contract_id):

    form = PlannedProjectsForm()
    contract = PlannedProj.query.get_or_404(contract_id)
    if form.validate_on_submit():

        if form.video_link.data and form.video_link.data != "N/A":
            match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data) 
            video_id_youtube = match.group(1)
            image_url = "https://img.youtube.com/vi/" + \
                video_id_youtube + "/mqdefault.jpg" 
            img_data = requests.get(image_url).content
            random_hex = secrets.token_hex(16)
            thumb_filename = random_hex + ".jpg"
            video_link = form.video_link.data
            video_thumb = thumb_filename
            with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
                handler.write(img_data)      
        else:
            video_link = "N/A"
            video_thumb = "N/A"

        contract.region = form.region.data or "N/A"
        contract.project = form.project.data or "N/A"
        contract.contractor = form.contractor.data or "N/A"
        contract.category = form.category.data or 'N/A'
        contract.revised_date = form.revised_date.data or None
        contract.length = form.length.data or 'N/A'
        contract.date_completed = form.date_completed.data or None
        contract.date_commenced = form.date_commenced.data or None
        contract.revised_sum = form.revised_sum.data or None
        contract.contract_sum = form.contract_sum.data or None
        contract.amt_to_date = form.amt_to_date.data or None
        contract.video_description = form.video_description.data or "N/A"
        contract.video_title = form.video_title.data or "N/A"
        contract.video_link = video_link
        contract.video_thumb = video_thumb
        
               
        # saving to database
        db.session.commit()
        flash('Project Updated successfully', 'success')
        return redirect(url_for('admin.planned_proj_list'))

    elif request.method == "GET":
        
        form.region.data = contract.region
        form.project.data = contract.project
        form.contractor.data = contract.contractor
        form.category.data = contract.category
        form.revised_date.data = contract.revised_date
        form.length.data = contract.length
        form.date_completed.data = contract.date_completed
        form.date_commenced.data = contract.date_commenced
        form.revised_sum.data = contract.revised_sum
        form.contract_sum.data = contract.contract_sum
        form.amt_to_date.data = contract.amt_to_date
        form.video_description.data =  contract.video_description
        form.video_title.data = contract.video_title
        form.video_link.data = contract.video_link


    return render_template('admin/planned_proj-edit.html', form=form, contract=contract, contract_id=contract_id)

@admin.route('/ongoing/project_list')
@login_required
@admin_required
def ongoing_proj_list():
    ongoing_list = OngoingProj.query.all()

    return render_template('admin/ongoing_proj_list.html', ongoing_list=ongoing_list)


@admin.route('/completed/project_list')
@login_required
@admin_required
def completed_proj_list():
    completed_list = CompletedProj.query.all()

    return render_template('admin/completed_proj_list.html', completed_list=completed_list)

@admin.route('/planned/project_list')
@login_required
@admin_required
def planned_proj_list():
    planned_list = PlannedProj.query.all()

    return render_template('admin/planned_proj_list.html', planned_list=planned_list)


@admin.route('/staff_details/<int:staff_id>/view_staff', methods=['GET', 'POST'])
def edit_staff(staff_id):

    staff = User.query.get_or_404(staff_id)
    form = UpdateStaffForm(obj=staff)
    if form.validate_on_submit():
        if form.picture.data:
            staff_pic = save_picture(form.picture.data)
            staff.image_file = staff_pic
        staff.ref_no = form.ref_no.data
        staff.acc_gen_no = form.acc_gen.data
        staff.ssf_no = form.ssf.data
        staff.name = form.name.data
        staff.dob = form.dob.data
        staff.sex = form.sex.data
        staff.job_pos = form.job_pos.data
        staff.date_engaged = form.date_engaged.data
        staff.pres_appt = form.pres_appt.data
        staff.station = form.division.data
        staff.email = form.email.data

        db.session.commit()
        flash('Account has been updated!', 'success')
        return redirect(url_for('admin.edit_staff', staff_id=staff.id))

    elif request.method == 'GET':
        form.ref_no.data = staff.ref_no
        form.acc_gen.data = staff.acc_gen_no
        form.ssf.data = staff.ssf_no
        form.name.data = staff.name
        form.dob.data = staff.dob
        form.sex.data = staff.sex
        form.job_pos.data = staff.job_pos
        form.date_engaged.data = staff.date_engaged
        form.pres_appt.data = staff.pres_appt
        form.division.data = staff.station
        form.email.data = staff.email
        form.picture.data=staff.image_file
        user_file = form.picture.data
        
    return render_template('admin/update_staff.html', form=form, staff=staff, user_file=user_file)


