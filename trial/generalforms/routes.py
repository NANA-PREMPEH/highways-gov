from flask import render_template, redirect, url_for, flash, send_file, make_response, Blueprint, request
from flask_login import current_user
import flask_login
from flask_login.utils import login_required
from trial import db
from trial.generalforms.forms import DefectReportForm, LeaveForm
from trial.models import Leave, Post 
import pdfkit


generalforms = Blueprint('generalforms', __name__) 
 

#Create a route for defect form
@generalforms.route('/defect', methods=['GET', 'POST'])
def defect():
    form = DefectReportForm()
    if form.validate_on_submit():
        flash(f'Defect Report Form submitted successfully', 'success') 
        return redirect(url_for('generalforms.defect'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('generalforms/defect_rep.html', title='Road Defects Report', form=form, posts=posts)

#Create a route for leave Form    
@generalforms.route('/leave', methods=['GET', 'POST']) 
@login_required
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        name=request.form.get('name')
        le_ave = Leave(name=name, rank=form.rank.data, section=form.section.data, date_app=form.date_app.data,
                    tele_no=form.tele_no.data, leave_cat=form.leave_cat.data, no_of_days=form.no_of_days.data, 
                    start_date=form.start_date.data, end_date=form.end_date.data, supp_info=form.supp_info.data,
                    address=form.address.data, mobile_no=form.mobile_no.data, email=form.email.data, 
                    days_proceed=form.days_proceed.data, effec_date=form.effec_date.data, resump_date=form.resump_date.data,
                    outs_days=form.outs_days.data, leave_status=form.leavestatus.data, author=current_user)
        db.session.add(le_ave)
        db.session.commit()
        flash(f"Leave form submitted successfully", 'success')
        return redirect(url_for('generalforms.view_form', post_id=le_ave.id))
    posts = Post.query.order_by(Post.id.desc()).all() 
    return render_template('generalforms/leave_form.html', title='Leave Form Report', form=form, posts=posts)



#Route to view the Leave form
@generalforms.route('/post/<int:post_id>') 
@login_required
def post(post_id):
    post = Leave.query.get_or_404(post_id)
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('generalforms/render_form.html', post=post, posts=posts)

#Route for View form 
@generalforms.route('/view_form/<int:post_id>', methods=['GET', 'POST']) 
@login_required
def view_form(post_id):
    post = Leave.query.get_or_404(post_id)
    posts = Post.query.order_by(Post.id.desc()).all()
    
    return render_template('generalforms/view_lv_form.html', title='Leave', post=post, posts=posts) 

#Generate pdf from the Leave Form
@generalforms.route('/get_pdf/<int:post_id>', methods=['GET','POST'])
@login_required
def get_pdf(post_id):

    post = Leave.query.get_or_404(post_id)
    posts = Post.query.order_by(Post.id.desc()).all()
    rendered= render_template('generalforms/render_form.html', title=current_user.name, post=post, posts=posts)
    css = ['trial/static/css/bootstrap.min.css', 'trial/static/css/style.css']

    options = {'enable-local-file-access': None}
    pdf = pdfkit.from_string(rendered, False, options=options, css=css)
    response = make_response(pdf)
    
    response.headers['content-Type'] = 'application/pdf'
    response.headers['content-Disposition'] = 'inline; filename=output.pdf'

    return response

#Render pdf format of the Leave Form
@generalforms.route('/render/<int:post_id>', methods=['GET', 'POST'])
def render(post_id):
    post = Leave.query.get_or_404(post_id)
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('generalforms/render_form.html', post=post, title=current_user.name, posts=posts)


#Route to view other forms   
@generalforms.route('/other_forms', methods=['GET', 'POST'])
@login_required
def others():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('generalforms/other_forms.html', title='Other Forms', posts=posts)

#Route to download Hospital Form
@generalforms.route('/download_hospital-form')
@login_required
def download_hosp():
    p = './static/other_forms/GHANA HIGHWAY AUTHORITY (HOSPITAL FORM).pdf'

    return send_file(p, as_attachment=True)

#Route to download Accomodation Form
@generalforms.route('/download_accomodation-form')
@login_required     
def download_accom():
    p = './static/other_forms/GHANA HIGHWAY AUTHORITY (REQUEST FOR ACCOMODATION).pdf'

    return send_file(p, as_attachment=True)