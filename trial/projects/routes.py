from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from trial import db
from flask_login import current_user
from trial.models import Post, Contract, Rehabilitation, Regravelling, Upgrading, Construction
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


#View Contract list from the database
@projects.route('/contract/view/<int:contract_id>/details') 
def view_contract(contract_id):
    contract = Contract.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", contract.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/video.html', contract=contract, contract_id=contract_id, posts=posts)
