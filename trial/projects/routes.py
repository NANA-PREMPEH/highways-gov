from flask import render_template, redirect, url_for, Blueprint, jsonify
from flask.globals import request
from trial import db
from trial.models import (Decongestion, Grading, Partialreconstruction, Post, Contract, Rehabilitation, Regravelling, Roadcondition, Supply, Upgrading, Construction,
                            Preconstruction, Resealing, Resurfacing, Repairs, Asphalticoverlay, Roadcondition2K19)
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
        return jsonify({'data': render_template('projects/completed/tables_json.html', q=q, form=form)})

    return render_template('projects/completed/tables.html', title='Basic', posts=posts, contract=contract, form=form)


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


@projects.route('/completed/periodic/rehabilitation', methods=['GET', 'POST']) 
def rehabilitation():
    form = DateForm()
    rehab_list = Rehabilitation.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d").strftime("%Y-%m-%d") 
        end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d").strftime("%Y-%m-%d")  

        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM rehabilitation \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/rehab_json.html', q=q, form=form)})

    return render_template('projects/completed/rehabilitation.html', title='Rehabilitation', rehab_list=rehab_list, posts=posts, form=form)

@projects.route('/completed/periodic/resealing', methods=['GET', 'POST']) 
def resealing():
    form = DateForm()
    reseal_list = Resealing.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM resealing \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/reseal_json.html', q=q, form=form)})

    return render_template('projects/completed/resealing.html', title='Resealing', reseal_list=reseal_list, posts=posts, form=form)

@projects.route('/completed/periodic/resurfacing', methods=['GET', 'POST']) 
def resurfacing():
    form = DateForm()
    resurface_list = Resurfacing.query.all()
    posts = Post.query.order_by(Post.id.desc()).all() 
    
    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM resurfacing \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/resurface_json.html', q=q, form=form)})

    return render_template('projects/completed/resurfacing.html', title='Resurfacing', resurface_list=resurface_list, posts=posts, form=form)

@projects.route('/completed/periodic/repairs_asphaltic', methods=['GET', 'POST'])
def repairs_asphaltic():
    form = DateForm()
    repairs_list = Repairs.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM repairs \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/repairs_json.html', q=q, form=form)})

    return render_template('projects/completed/repairs_asphaltic.html', title='Repairs & Asphaltic', repairs_list=repairs_list, posts=posts, form=form)

@projects.route('/completed/periodic/preconstruction', methods=['GET', 'POST'])
def preconstruct():
    form = DateForm()
    precons_list = Preconstruction.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM preconstruction \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/precons_json.html', q=q, form=form)})

    return render_template('projects/completed/preconstruction.html', title='Preconstruction', precons_list=precons_list, posts=posts, form=form)

@projects.route('/completed/periodic/asphalticoverlay', methods=['GET', 'POST'])
def asphalticoverlay():
    form = DateForm()
    overlay_list = Asphalticoverlay.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM asphalticoverlay \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/asphaltic_json.html', q=q, form=form)})

    return render_template('projects/completed/asphaltic_overlay.html', title='Asphaltic Overlay', overlay_list=overlay_list, posts=posts, form=form)

@projects.route('/completed/periodic/upgrading', methods=['GET', 'POST'])
def upgrading(): 
    form = DateForm()
    upgrade_list = Upgrading.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM upgrading \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/upgrade_json.html', q=q, form=form)})
    return render_template('projects/completed/upgrading.html', title='Upgrading', upgrade_list=upgrade_list, posts=posts, form=form)

@projects.route('/completed/periodic/decongestion', methods=['GET', 'POST'])
def decongestion(): 
    form = DateForm()
    deconges_list = Decongestion.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM decongestion \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/decongestion_json.html', q=q, form=form)})
    return render_template('projects/completed/decongestion.html', title='Decongestion', deconges_list=deconges_list, posts=posts, form=form)


@projects.route('/completed/periodic/supply_inst', methods=['GET', 'POST'])
def supply(): 
    form = DateForm()
    supply_list = Supply.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM supply \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/supply_json.html', q=q, form=form)})
    return render_template('projects/completed/supply.html', title='Supply & Installation of Materials', supply_list=supply_list, posts=posts, form=form)

@projects.route('/completed/periodic/partial_reconst', methods=['GET', 'POST'])
def part_reconst(): 
    form = DateForm()
    part_reconst_list = Partialreconstruction.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM partialreconstruction \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/partial_reconst_json.html', q=q, form=form)})
    return render_template('projects/completed/partial_reconst.html', title='Partial Reconstruction', part_reconst_list=part_reconst_list, posts=posts, form=form)

@projects.route('/completed/periodic/grading_proj', methods=['GET', 'POST'])
def grading(): 
    form = DateForm()
    grading_list = Grading.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM partialreconstruction \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/grading_json.html', q=q, form=form)})
    return render_template('projects/completed/grading.html', title='grading', grading_list=grading_list, posts=posts, form=form)

@projects.route('/completed/periodic/construction', methods=['GET', 'POST'])
def construction():
    form = DateForm()
    const_list = Construction.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM construction \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/const_json.html', q=q, form=form)})

    return render_template('projects/completed/construction.html', title='Construction', const_list=const_list, posts=posts, form=form)

@projects.route('/completed/periodic/regravelling', methods=['GET', 'POST'])
def regravelling():
    form = DateForm()
    regrav_list = Regravelling.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM regravelling \
                                    WHERE date_commenced >= %s  and date_completed<= %s) t1",\
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/regrav_json.html', q=q, form=form)})

    return render_template('projects/completed/regravelling.html', title='Regravelling', regrav_list=regrav_list, posts=posts, form=form)

@projects.route('/reports_2018')
def reports_2018():
    rd_cond = Roadcondition.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/reports_2018.html', title='2018 Report',  posts=posts, rd_cond=rd_cond)

@projects.route('/reports_2019')
def reports_2019():
    rd_cond = Roadcondition2K19.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/reports_2019.html', title='2019 Report',  posts=posts, rd_cond=rd_cond)

@projects.route('/projects/critical_roads')
def critical_roads():
    posts = Post.query.order_by(Post.id.desc()).all()

    return render_template('projects/completed/critical_roads.html', posts=posts) 



#View Regravelling Projects details from the database
@projects.route('/regrav/view/<int:contract_id>/details')  
def regrav_contract(contract_id):
    regrav = Regravelling.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", regrav.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/regrav_details.html', regrav=regrav, contract_id=contract_id, posts=posts)

#View Regravelling Projects details from the database
@projects.route('/grading/view/<int:contract_id>/details')  
def grading_contract(contract_id):
    grading = Grading.query.get_or_404(contract_id)
 
    match = re.search(r"youtube\.com/.*v=([^&]*)", grading.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/grading_details.html', grading=grading, contract_id=contract_id, posts=posts)

#View Rehabilitation Projects details from the database
@projects.route('/rehab/view/<int:contract_id>/details') 
def rehab_contract(contract_id):
    rehab = Rehabilitation.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", rehab.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/rehab_details.html', rehab=rehab, contract_id=contract_id, posts=posts)

#View Supply and Installation Projects details from the database
@projects.route('/supply_inst/view/<int:contract_id>/details') 
def supply_contract(contract_id):
    supply = Supply.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", supply.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/supply_details.html', supply=supply, contract_id=contract_id, posts=posts)

#View Partial Reconstruction Projects details from the database
@projects.route('/partial_reconst/view/<int:contract_id>/details') 
def partial_reconst(contract_id):
    part_reconst = Partialreconstruction.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", part_reconst.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/part_reconst_details.html', part_reconst=part_reconst, contract_id=contract_id, posts=posts)


#View Decongestion Projects details from the database
@projects.route('/decongestion/view/<int:contract_id>/details') 
def deconges_view(contract_id):
    decongest = Decongestion.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", decongest.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/decongestion_details.html', decongest=decongest, contract_id=contract_id, posts=posts)

#View Asphaltic Overlay Projects details from the database
@projects.route('/asphaltic/view/<int:contract_id>/details') 
def asphaltic_contract(contract_id):
    asphaltic = Asphalticoverlay.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", asphaltic.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/asphaltic_details.html', asphaltic=asphaltic, contract_id=contract_id, posts=posts)
    
#View Construction Projects details from the database
@projects.route('/const/view/<int:contract_id>/details') 
def const_contract(contract_id):
    const = Construction.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", const.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/const_details.html', const=const, contract_id=contract_id, posts=posts)

#View Pre-Construction Projects details from the database
@projects.route('/precons/view/<int:contract_id>/details') 
def precons_contract(contract_id):
    precons = Preconstruction.query.get_or_404(contract_id) 

    match = re.search(r"youtube\.com/.*v=([^&]*)", precons.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/precons_details.html', precons=precons, contract_id=contract_id, posts=posts)

#View Repairs & Asphaltic Projects details from the database
@projects.route('/repairs/view/<int:contract_id>/details') 
def repairs_contract(contract_id):
    repairs = Repairs.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", repairs.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/repairs_details.html', repairs=repairs, contract_id=contract_id, posts=posts)

#View Resealing Projects details from the database
@projects.route('/reseal/view/<int:contract_id>/details') 
def reseal_contract(contract_id):
    reseal = Resealing.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", reseal.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/reseal_details.html', reseal=reseal, contract_id=contract_id, posts=posts)

#View Resurfacing Projects details from the database
@projects.route('/resurface/view/<int:contract_id>/details') 
def resurface_contract(contract_id):
    resurface = Resurfacing.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", resurface.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/resurface_details.html', resurface=resurface, contract_id=contract_id, posts=posts)

#View Upgrading Projects details from the database
@projects.route('/upgrade/view/<int:contract_id>/details')  
def upgrade_contract(contract_id):
    upgrade = Upgrading.query.get_or_404(contract_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", upgrade.video_link)
    contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/upgrade_details.html', upgrade=upgrade, contract_id=contract_id, posts=posts)



