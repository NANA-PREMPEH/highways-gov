from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from trial import db
from flask_login import current_user
from trial.models import Post, Contract, Rehabilitation, Regravelling, Upgrading, Construction
from trial.projects.forms import ContractDetailsForm
from trial.projects.regrav import update_regrav, regrav_data
from trial.projects.rehab import update_rehab, rehab_data
from trial.projects.construc import update_construc, construc_data
from trial.projects.upgrage import update_upgrade, upgrade_data
import secrets
import re
import requests 

projects = Blueprint('projects', __name__) 



#Route to view Contract Lists
@projects.route('/table', methods=['GET', 'POST '])
def table():
    contract = Contract.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/tables.html', title='Basic', posts=posts, contract=contract)


@projects.route('/const')
def const():
    update_construc(construc_data)
    return redirect(url_for('main.home'))

@projects.route('/regrav')
def regrav():
    update_regrav(regrav_data)
    return redirect(url_for('main.home'))

@projects.route('/rehab')
def rehab():
    update_rehab(rehab_data)
    return redirect(url_for('main.home'))

@projects.route('/upgrade')
def upgrade():
    update_upgrade(upgrade_data)
    return redirect(url_for('main.home'))

@projects.route('/rehabilitation', methods=['GET', 'POST'])
def rehabilitation():
    rehab_list = Rehabilitation.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/rehabilitation.html', title='Rehabilitation', rehab_list=rehab_list, posts=posts)

@projects.route('/upgrading', methods=['GET', 'POST'])
def upgrading():
    upgrade_list = Upgrading.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/Upgrading.html', title='Upgrading', upgrade_list=upgrade_list, posts=posts)

@projects.route('/construction', methods=['GET', 'POST'])
def construction():
    const_list = Construction.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/construction.html', title='Construction', const_list=const_list, posts=posts)

@projects.route('/regravelling', methods=['GET', 'POST'])
def regravelling():
    regrav_list = Regravelling.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/regravelling.html', title='Regravelling', regrav_list=regrav_list, posts=posts)

#Add new Contract details to the database
@projects.route('/add_contract', methods=['GET', 'POST'])
def add_contract():

    form = ContractDetailsForm()

    if form.validate_on_submit():
    
        match = re.search(r"youtube\.com/.*v=([^&]*)", form.video_link.data)
        video_id_youtube = match.group(1)

        image_url = "https://img.youtube.com/vi/" + \
            video_id_youtube + "/mqdefault.jpg" 
        img_data = requests.get(image_url).content
        random_hex = secrets.token_hex(16)
        thumb_filename = random_hex + ".jpg"

        with open(current_app.root_path + '/static/thumbs/' + thumb_filename, 'wb') as handler:
            handler.write(img_data)

        uploaded_details = Contract(name_of_contract=form.name_of_contract.data, length=form.length.data, 
                                          lot=form.lot.data, contract_sum=form.contract_sum.data, 
                                          contractor=form.contractor.data, date_commenced=form.date_commenced.data, 
                                          date_completed=form.date_completed.data, video_title=form.video_title.data, 
                                          video_link=form.video_link.data, video_description=form.video_description.data,
                                          video_thumb=thumb_filename, user_id=current_user.id)

        # saving to database
        db.session.add(uploaded_details)
        db.session.commit()
        flash('Data added successfully', 'success')
        return redirect(url_for('projects.add_contract'))

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/contract_details-form.html', form=form,  posts=posts)

#View Contract list from the database
@projects.route('/contract/view/<int:contract_id>/details')
def view_contract(contract_id):
    contract = Contract.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", contract.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/video.html', contract=contract, contract_id=contract_id, posts=posts)
