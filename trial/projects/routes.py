from flask import render_template, redirect, url_for, Blueprint, jsonify
from flask.globals import request
from trial import db
from trial.models import (Post, Contract, Rehabilitation, Regravelling, Upgrading, Construction,
                            Preconstruction, Resealing, Resurfacing, Repairs, Asphalticoverlay)
from trial.projects.regrav import update_regrav, regrav_data
from trial.projects.rehab import update_rehab, rehab_data
from trial.projects.construc import update_construc, construc_data
from trial.projects.upgrage import update_upgrade, upgrade_data
from trial.projects.reseal import update_reseal, reseal_data
from trial.projects.overlay import update_overlay, overlay_data
from trial.projects.precons import update_precons, precons_data
from trial.projects.repairs import update_repairs, repairs_data
from trial.projects.resurface import update_resurface, resurface_data
from trial.projects.forms import DateForm
import re
from datetime import datetime

projects = Blueprint('projects', __name__) 



#Route to view Contract Lists
@projects.route('/table', methods=['GET', 'POST'])
def table():
    form = DateForm()
    
    contract = Contract.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()        
    
    if request.method == "POST":
        start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d").strftime("%Y-%m-%d") 
        end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d").strftime("%Y-%m-%d")  
        q = db.session.query(db.func.sum(Contract.contract_sum)).filter(Contract.date_commenced>=start_date).filter(Contract.date_completed<=end_date).first()
        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/tables.html', title='Basic', posts=posts, contract=contract, form=form)


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
def rehab():
    update_rehab(rehab_data)
    return redirect(url_for('main.home'))

@projects.route('/upgrade')
def upgrade():
    update_upgrade(upgrade_data)
    return redirect(url_for('main.home'))

@projects.route('/completed/periodic/rehabilitation', methods=['GET', 'POST'])
def rehabilitation():
    form = DateForm()
    rehab_list = Rehabilitation.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d").strftime("%Y-%m-%d") 
        end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d").strftime("%Y-%m-%d")  

        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM resealing \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/rehabilitation.html', title='Rehabilitation', rehab_list=rehab_list, posts=posts, form=form)

@projects.route('/completed/periodic/resealing', methods=['GET', 'POST'])
def resealing():
    form = DateForm()
    reseal_list = Resealing.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM resealing \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/resealing.html', title='Resealing', reseal_list=reseal_list, posts=posts, form=form)

@projects.route('/completed/periodic/resurfacing', methods=['GET', 'POST']) 
def resurfacing():
    form = DateForm()
    resurface_list = Resurfacing.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    
    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM resurfacing \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/resurfacing.html', title='Resurfacing', resurface_list=resurface_list, posts=posts, form=form)

@projects.route('/completed/periodic/repairs_asphaltic', methods=['GET', 'POST'])
def repairs_asphaltic():
    form = DateForm()
    repairs_list = Repairs.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM repairs \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/repairs_asphaltic.html', title='Repairs & Asphaltic', repairs_list=repairs_list, posts=posts, form=form)

@projects.route('/completed/periodic/preconstruction', methods=['GET', 'POST'])
def preconstruct():
    form = DateForm()
    precons_list = Preconstruction.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM preconstruction \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/preconstruction.html', title='Preconstruction', precons_list=precons_list, posts=posts, form=form)

@projects.route('/completed/periodic/asphalticoverlay', methods=['GET', 'POST'])
def asphalticoverlay():
    form = DateForm()
    overlay_list = Asphalticoverlay.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM asphalticoverlay \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/asphaltic_overlay.html', title='Asphaltic Overlay', overlay_list=overlay_list, posts=posts, form=form)

@projects.route('/completed/periodic/upgrading', methods=['GET', 'POST'])
def upgrading(): 
    form = DateForm()
    upgrade_list = Upgrading.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM upgrading \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})
    return render_template('projects/upgrading.html', title='Upgrading', upgrade_list=upgrade_list, posts=posts, form=form)

@projects.route('/completed/periodic/construction', methods=['GET', 'POST'])
def construction():
    form = DateForm()
    const_list = Construction.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM construction \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/construction.html', title='Construction', const_list=const_list, posts=posts, form=form)

@projects.route('/completed/periodic/regravelling', methods=['GET', 'POST'])
def regravelling():
    form = DateForm()
    regrav_list = Regravelling.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(contract_sum),0) As col_total FROM regravelling \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/tables_json.html', q=q, form=form)})

    return render_template('projects/regravelling.html', title='Regravelling', regrav_list=regrav_list, posts=posts, form=form)

@projects.route('/reports')
def reports():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/reports.html', title='Report',  posts=posts)


#View Contract list from the database
@projects.route('/contract/view/<int:contract_id>/details') 
def view_contract(contract_id):
    contract = Contract.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", contract.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/video.html', contract=contract, contract_id=contract_id, posts=posts)
