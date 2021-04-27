from flask import render_template, redirect, url_for, Blueprint, jsonify
from flask.globals import request
from trial import db
from trial.models import Post, Roadcondition, Roadcondition2K19
from trial.projects.regrav import update_regrav, regrav_data
from trial.projects.rehab import update_rehab, rehab_data
from trial.projects.construc import update_construc, construc_data
from trial.projects.upgrage import update_upgrade, upgrade_data
from trial.projects.reseal import update_reseal, reseal_data
from trial.projects.overlay import update_overlay, overlay_data
from trial.projects.precons import update_precons, precons_data
from trial.projects.repairs import update_repairs, repairs_data
from trial.projects.resurface import update_resurface, resurface_data
from trial.road_conditions import rd_cond_data, update_rd_cond
from trial.road_cond_2k19 import road_data_2K19, update_rd_cond2K19 
from trial.projects.forms import DateForm
from flask_login import login_required
from trial.users.utils import admin_required
import re
from datetime import datetime

projects = Blueprint('projects', __name__) 


@projects.route('/const')
def const():
    update_construc(construc_data)
    return redirect(url_for('main.home'))

@projects.route('/regrav')
def regrav():
    update_regrav(regrav_data)
    return redirect(url_for('main.home'))

@projects.route('/reseal')
def reseal():
    update_reseal(reseal_data)
    return redirect(url_for('main.home'))

@projects.route('/repairs')
def repairs():
    update_repairs(repairs_data)
    return redirect(url_for('main.home'))

@projects.route('/resurface')
def resurface():
    update_resurface(resurface_data)
    return redirect(url_for('main.home'))

@projects.route('/precons')
def precons():
    update_precons(precons_data)
    return redirect(url_for('main.home'))

@projects.route('/overlay')
def overlay():
    update_overlay(overlay_data)
    return redirect(url_for('main.home'))

@projects.route('/rehab')
@login_required
@admin_required
def rehab():
    update_rehab(rehab_data)
    return redirect(url_for('main.home'))

@projects.route('/upgrade')
def upgrade():
    update_upgrade(upgrade_data)
    return redirect(url_for('main.home'))

@projects.route('/road_cond')
def road_cond(): 
    update_rd_cond(rd_cond_data)
    return redirect(url_for('main.home'))

@projects.route('/road_cond_2K19')
def road_cond_2K19():
    update_rd_cond2K19(road_data_2K19)
    return redirect(url_for('main.home'))



@projects.route('/reports_2018')
def reports_2018():
    rd_cond = Roadcondition.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/reports_2018.html', title='2018 Report',  posts=posts, rd_cond=rd_cond)

@projects.route('/reports_2019')
def reports_2019():
    rd_cond = Roadcondition2K19.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/reports_2019.html', title='2019 Report',  posts=posts, rd_cond=rd_cond)

@projects.route('/projects/critical_roads')
def critical_roads():
    posts = Post.query.order_by(Post.id.desc()).all()

    return render_template('projects/critical_roads.html', posts=posts) 






