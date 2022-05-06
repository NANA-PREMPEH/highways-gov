from datetime import datetime, date
import secrets
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, jsonify
from flask_login import current_user, logout_user, login_required
from trial.models import (CompletedProj, Post, OngoingProj, User, TerminatedProj, 
                            AwardedProj, PlannedProj, Gallery, EmployeeDetails)
from trial.admin.forms import (RegistrationForm, BlogPostForm, CompletedProjectsForm, UpdateStaffForm, OngoingProjectsForm, 
                                PlannedProjectsForm,TerminatedProjectsForm, AwardedProjectsForm, GalleryForm)
from trial.admin.utils import save_photo, save_picture, save_proj_image, save_gallery_image
import re
import requests
from trial import db, bcrypt 
from trial.users.utils import admin_required
import  json


admin = Blueprint('admin', __name__) 



@admin.route('/dashboard')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')


#Register Employees
@admin.route('/register_staff', methods=['GET', 'POST'])
@login_required
@admin_required
def register_staff():

    if request.method == 'POST':
        profile_pic = request.files.get('profile_pic')    
        new_json_val = request.form.get('json_data')
        dict_items = json.loads(new_json_val)     
        profile_url = request.form.get('profile_url')  

        surname = request.form.get('surname')
        mid_name = request.form.get('mid_name')
        first_name = request.form.get('first_name')
        email = request.form.get('email')
        mobile_no = request.form.get('mobile_no')
        emp_dob = request.form.get('emp_dob') 
        birth_place = request.form.get('birth_place')  
        date_engaged = request.form.get('date_engaged')  
        mar_status = request.form.get('mar_status')
        gender = request.form.get('gender')
        staff_no = request.form.get('staff_no')
        seniority = request.form.get('seniority')
        ssnit_no = request.form.get('ssnit_no')
        hofl_no = request.form.get('hofl_no')
        emp_status = request.form.get('emp_status')
        home_add = request.form.get('home_add')
        category = request.form.get('category')
        catbydiv = request.form.get('catbydiv')
        languages = request.form.get('languages')
        nok_name = request.form.get('nok_name')
        nok_rel = request.form.get('nok_rel')
        nok_add = request.form.get('nok_add')
        dad_name = request.form.get('dad_name')
        dad_status = request.form.get('dad_status')
        mum_name = request.form.get('mum_name')
        mum_status = request.form.get('mum_status')

        if profile_pic is not None: 
            profile_image = save_picture(profile_pic) 
        else:
            profile_image = 'default.jpg'

        postings = {
            'postings': dict_items['postings']
        }
        promotion = {
            'promotion': dict_items['promotion']
        }
        education = {
            'education': dict_items['education']
        }
        dependants = {
            'dependants': dict_items['dependants']
        }
        workexperience = {
            'workexperience': dict_items['workexperience']
        }
        
        
        
        
        new_val = EmployeeDetails(surname=surname, mid_name=mid_name, first_name=first_name, email=email, 
                                    mobile_no=mobile_no, emp_dob=emp_dob, birth_place=birth_place, 
                                    mar_status=mar_status, gender=gender, staff_no=staff_no, ssnit_no=ssnit_no,
                                    hofl_no=hofl_no, emp_status=emp_status, home_add=home_add,
                                    languages=languages, nok_name=nok_name, nok_rel=nok_rel, nok_add=nok_add,
                                    dad_name=dad_name, dad_status=dad_status, mum_name=mum_name, 
                                    mum_status=mum_status, dependants=dependants, postings=postings,
                                    workexperience=workexperience, promotion=promotion, education=education,
                                    profile_image=profile_image, new_json_val=new_json_val, category=category,
                                    catbydiv=catbydiv, date_engaged=date_engaged, seniority=seniority) 
        db.session.add(new_val)
        db.session.commit()
        msg = 'New record created successfully'
        flash('Data has been recorded successfully', 'success')
        return jsonify(msg)
    
    return render_template('admin/register_staff.html', title='Register') 

#View All employee list in Dashboard
@admin.route('/admin/dashboard/view_employee_list')
@login_required
def admin_view_employee_list():
    empl = EmployeeDetails.query.all()
    today = date.today()
    return render_template('admin/view_employee_list.html', title='Employee List', 
                            empl=empl, datetime=datetime, today=today)

@admin.route('/admin/employee/<int:id>/delete_details', methods=['POST'])
@login_required
def delete_employee(id):
    empl = EmployeeDetails.query.get_or_404(id)
    db.session.delete(empl)
    db.session.commit()
    flash('Employee has been deleted successfully!', 'success')
    return redirect(url_for('admin.admin_view_employee_list'))

#Update Gallery
@admin.route('/add_image', methods=['GET', 'POST'])
@login_required
def add_image():
    form = GalleryForm()
    if form.validate_on_submit():
        picture = save_gallery_image(form.picture.data)
        pic = Gallery(image_file=picture)
        db.session.add(pic)
        db.session.commit()
        flash(f"Image added successfully", 'success')
    return render_template('admin/gallery_pics.html', form=form)

#Update Blog Post
@admin.route('/blog_post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_blog_post(post_id):
    form = BlogPostForm()
    blog_post = Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.body = form.blog_content.data
        blog_post.pub_date = datetime.utcnow() 
        blog_post.user_id = current_user.id
        if form.picture.data:
            picture = save_photo(form.picture.data)
            blog_post.image = picture
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(request.url) 
    form.title.data = blog_post.title
    form.blog_content.data = blog_post.body
    form.picture.data = blog_post.image
    return render_template('admin/update_blog_post.html', form=form)

#Delete Blog Post
@admin.route('/blog_post/<int:id>/delete', methods=['POST'])
def delete_blog_post(id):
    blog_post = Post.query.get_or_404(id)

    db.session.delete(blog_post)
    db.session.commit()

    flash('Post has been deleted successfully!', 'success')
    return redirect(request.referrer)

#Return list of Blog Posts
@admin.route('/blog/blog_posts')
def blog_posts():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('admin/blog_posts.html', posts=posts)

#Return list of Gallery Images
@admin.route('/gallery')
def gallery():
    pics = Gallery.query.all()
    return render_template('admin/gallery.html', title='Gallery', pics=pics)

#Update Image
#Update Blog Post
@admin.route('/image/<int:image_id>/update', methods=['GET', 'POST'])
@login_required
def update_image(image_id):
    form = GalleryForm()
    pic = Gallery.query.get_or_404(image_id)
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_gallery_image(form.picture.data)
            pic.image_file = picture
        db.session.commit()
        flash('Image has been updated!', 'success')
        return redirect(request.url)
    return render_template('admin/update_image.html', form=form, pic=pic)

#Delete Images
@admin.route('/image/<int:id>/delete', methods=['POST'])
def delete_image(id):
    image = Gallery.query.get_or_404(id)

    db.session.delete(image)
    db.session.commit()
    flash('Image has been deleted successfully!', 'success')
    return redirect(request.referrer)

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
        
        funding = form.funding.data or "N/A"
        procurement = form.procurement.data or "N/A"
        # contractor = form.contractor.data or "N/A"
        award_date = form.award_date.data or "N/A"
        revised_date = form.revised_date.data or "N/A"
        revised_sum = form.revised_sum.data or "N/A"
        cost_to_complete = form.cost_to_complete.data or "N/A"
        physical = form.physical.data or "N/A"
        time_elapsed = form.time_elapsed.data or "N/A"
        activity = form.activity.data or "N/A"
        phy = form.phy.data or "N/A"
        remarks = form.remarks.data or "N/A"
        category = request.form.get('completed_periodic') or 'N/A' 
        length = form.length.data or 'N/A'
        date_completed = form.date_completed.data or None
        date_commenced = form.date_commenced.data or None
        contract_sum = form.contract_sum.data or None
        amt_to_date = form.amt_to_date.data or None
        video_description = form.video_description.data or "N/A"
        video_title = form.video_title.data or "N/A"

        uploaded_details = CompletedProj(region=form.region.data, project=form.project.data, length=length,
                                            funding=funding, procurement=procurement, award_date=award_date,
                                            revised_date=revised_date, revised_sum=revised_sum, cost_to_complete=cost_to_complete,
                                            physical=physical, time_elapsed=time_elapsed, activity=activity, phy=phy, remarks=remarks, 
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


#Update Contract details in database(Ongoing)
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
        contract.status = request.form.get('ongoing_status')
        contract.procurement = form.procurement.data
        contract.award_date = form.award_date.data
        contract.cost_to_complete = form.cost_to_complete.data
        contract.physical = form.physical.data
        contract.time_elapsed = form.time_elapsed.data
        contract.remarks = form.remarks.data
        contract.funding = form.funding.data
        
        #If status is changed to Completed, Ongoing Contract is moved to Completed Projects
        if request.form.get('ongoing_status') == 'Project Completed':
            uploaded_details = CompletedProj(region=form.region.data, project=form.project.data, 
                                            length=form.length.data or 'N/A', contractor=form.contractor.data or 'N/A', 
                                            category=form.category.data or 'N/A', date_commenced=form.date_commenced.data or None, 
                                            date_completed=form.date_completed.data or None, revised_date=form.revised_date.data or None, 
                                            contract_sum=form.contract_sum.data or None, revised_sum=form.revised_sum.data or None,
                                            amt_to_date=form.amt_to_date.data or None,video_title=form.video_title.data or "N/A",
                                            video_link=video_link,video_description=form.video_description.data or "N/A",
                                            procurement=form.procurement.data, award_date=form.award_date.data or None,
                                            cost_to_complete=form.cost_to_complete.data, 
                                            physical=form.physical.data, time_elapsed=form.time_elapsed.data,
                                            remarks=form.remarks.data, funding=form.funding.data,
                                            status= request.form.get('ongoing_status'), 
                                            video_thumb=video_thumb, user_id=current_user.id)
            db.session.add(uploaded_details)
               
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
        form.procurement.data = contract.procurement
        form.award_date.data = contract.award_date
        form.cost_to_complete.data = contract.cost_to_complete
        form.physical.data = contract.physical
        form.time_elapsed.data = contract.time_elapsed
        form.remarks.data = contract.remarks
        form.funding.data = contract.funding


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

        # Start of Additional data enrty items
        contract.funding = form.funding.data or "N/A"
        contract.procurement = form.procurement.data or "N/A"
        contract.award_date = form.award_date.data or None
        contract.revised_date = form.revised_date.data or None
        contract.cost_to_complete = form.cost_to_complete.data or "N/A"
        contract.physical = form.physical.data or None
        contract.time_elapsed = form.time_elapsed.data or None
        contract.phy = form.phy.data or None
        contract.activity = form.activity.data or "N/A"
        contract.remarks = form.remarks.data or "N/A"
        # end of Additional data enrty items
        contract.region = form.region.data or "N/A"
        contract.project = form.project.data or "N/A"
        contract.contractor = form.contractor.data or "N/A"
        contract.category = form.category.data or 'N/A'
        contract.length = form.length.data or 'N/A'
        contract.date_completed = form.date_completed.data or None
        contract.date_commenced = form.date_commenced.data or None
        contract.contract_sum = form.contract_sum.data or "N/A"
        contract.amt_to_date = form.amt_to_date.data or "N/A"
        contract.video_description = form.video_description.data or "N/A"
        contract.video_title = form.video_title.data or "N/A"
        contract.video_link = video_link
        contract.video_thumb = video_thumb
        
               
        # saving to database
        db.session.commit()
        flash('Project Updated successfully', 'success')
        return redirect(url_for('admin.completed_proj_list'))

    elif request.method == "GET":
        
        # populate project from the database
        # Start of Additional data enrty items
        form.funding.data = contract.funding
        form.procurement.data = contract.procurement
        form.award_date.data =  contract.award_date
        form.revised_date.data = contract.revised_date
        form.cost_to_complete.data = contract.cost_to_complete
        form.physical.data =  contract.physical
        form.time_elapsed.data = contract.time_elapsed
        form.phy.data = contract.phy
        form.activity.data = contract.activity
        form.remarks.data = contract.remarks
        # end of Additional data enrty items
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
        contract.status = request.form.get('planned_status')
        contract.procurement = form.procurement.data
        contract.award_date = form.award_date.data
        contract.cost_to_complete = form.cost_to_complete.data
        contract.physical = form.physical.data
        contract.time_elapsed = form.time_elapsed.data
        contract.remarks = form.remarks.data
        contract.funding = form.funding.data
        
        #If status is changed to Ongoing, Planned Contract is moved to Ongoing Projects
        if request.form.get('planned_status') == 'Project Ongoing':
            uploaded_details = OngoingProj(region=form.region.data, project=form.project.data, 
                                            length=form.length.data or 'N/A', contractor=form.contractor.data or 'N/A', 
                                            category=form.category.data or 'N/A', date_commenced=form.date_commenced.data or None, 
                                            date_completed=form.date_completed.data or None, revised_date=form.revised_date.data or None, 
                                            contract_sum=form.contract_sum.data or None, revised_sum=form.revised_sum.data or None,
                                            amt_to_date=form.amt_to_date.data or None,video_title=form.video_title.data or "N/A",
                                            video_link=video_link,video_description=form.video_description.data or "N/A",
                                            procurement=form.procurement.data, award_date=form.award_date.data or None,
                                            cost_to_complete=form.cost_to_complete.data, 
                                            physical=form.physical.data, time_elapsed=form.time_elapsed.data,
                                            remarks=form.remarks.data, funding=form.funding.data,
                                            status= request.form.get('planned_status'), 
                                            video_thumb=video_thumb, user_id=current_user.id)
            db.session.add(uploaded_details)   
               
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
        form.procurement.data = contract.procurement
        form.award_date.data = contract.award_date
        form.cost_to_complete.data = contract.cost_to_complete
        form.physical.data = contract.physical
        form.time_elapsed.data = contract.time_elapsed
        form.remarks.data = contract.remarks
        form.funding.data = contract.funding
        


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

#Edit Employee Details Form
@admin.route('/emp_details/<int:emp_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_emp_details(emp_id):

    emp = EmployeeDetails.query.get_or_404(emp_id)
    image = emp.profile_image
    value_1 = emp.new_json_val
    depe = json.loads(emp.new_json_val)

    
    if request.method == 'POST':

        new_json_val = request.form.get('json_data')
        dict_items = json.loads(new_json_val)

        profile_pic = request.files.get('profile_pic')    
        if profile_pic is not None: 
            emp.profile_image = save_picture(profile_pic)
        emp.surname = request.form.get('surname')
        emp.mid_name = request.form.get('mid_name')
        emp.first_name = request.form.get('first_name')
        emp.email = request.form.get('email')
        emp.mobile_no = request.form.get('mobile_no')
        emp.emp_dob = request.form.get('emp_dob') 
        emp.birth_place = request.form.get('birth_place')  
        emp.date_engaged = request.form.get('date_engaged')  
        emp.mar_status = request.form.get('mar_status')
        emp.gender = request.form.get('gender')
        emp.staff_no = request.form.get('staff_no')
        emp.seniority = request.form.get('seniority')
        emp.ssnit_no = request.form.get('ssnit_no')
        emp.hofl_no = request.form.get('hofl_no')
        emp.emp_status = request.form.get('emp_status')
        emp.home_add = request.form.get('home_add')
        emp.category = request.form.get('category')
        emp.catbydiv = request.form.get('catbydiv')
        emp.languages = request.form.get('languages')
        emp.nok_name = request.form.get('nok_name')
        emp.nok_rel = request.form.get('nok_rel')
        emp.nok_add = request.form.get('nok_add')
        emp.dad_name = request.form.get('dad_name')
        emp.dad_status = request.form.get('dad_status')
        emp.mum_name = request.form.get('mum_name')
        emp.mum_status = request.form.get('mum_status')
        emp.new_json_val = new_json_val

        postings = {
            'postings': dict_items['postings']
        }
        emp.postings = postings

        promotion = {
            'promotion': dict_items['promotion']
        }
        emp.promotion = promotion

        education = {
            'education': dict_items['education']
        }

        emp.education = education

        dependants = {
            'dependants': dict_items['dependants']
        }
        emp.dependants = dependants

        workexperience = {
            'workexperience': dict_items['workexperience']
        }
        emp.workexperience = workexperience

        db.session.commit()
        msg = 'New record created successfully'
        flash('Staff details updated successfully!', 'success')
        return jsonify(msg)

    return render_template('admin/update_emp_details.html',  emp=emp, image=image, value_1=value_1, depe=depe)



