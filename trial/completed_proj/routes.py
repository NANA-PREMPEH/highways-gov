from flask import render_template, redirect, request, Blueprint, jsonify
from trial import db
from datetime import datetime
from trial.models import Post, CompletedProj
import re

completed_proj = Blueprint('completed_proj', __name__)


@completed_proj.route('/completed/periodic/rehabilitation', methods=['GET', 'POST'])
def rehabilitation():
    rehab_list = CompletedProj.query.filter_by(category="Rehabilitation")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d").strftime("%Y-%m-%d") 
        end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d").strftime("%Y-%m-%d")  

        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Rehabilitation'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/rehab_json.html', q=q)})

    return render_template('projects/completed/rehabilitation.html', title='Rehabilitation', rehab_list=rehab_list, posts=posts)

@completed_proj.route('/completed/periodic/resealing', methods=['GET', 'POST']) 
def resealing():
    
    reseal_list = CompletedProj.query.filter_by(category="Resealing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Resealing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/reseal_json.html', q=q)})

    return render_template('projects/completed/resealing.html', title='Resealing', reseal_list=reseal_list, posts=posts)
@completed_proj.route('/completed/periodic/reconstruction', methods=['GET', 'POST']) 
def reconstruction():
    
    reconstruct_list = CompletedProj.query.filter_by(category="Reconstruction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Reconstruction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/reconstruct_json.html', q=q)})

    return render_template('projects/completed/reconstruction.html', title='Reconstruction', reconstruct_list=reconstruct_list, posts=posts)

@completed_proj.route('/completed/periodic/resurfacing', methods=['GET', 'POST']) 
def resurfacing():
    
    resurface_list = CompletedProj.query.filter_by(category="Resurfacing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Resurfacing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/resurface_json.html', q=q)})

    return render_template('projects/completed/resurfacing.html', title='Resurfacing', resurface_list=resurface_list, posts=posts)

@completed_proj.route('/completed/periodic/repairs_asphaltic', methods=['GET', 'POST']) 
def repairs_asphaltic():
    
    repairs_list = CompletedProj.query.filter_by(category="Repairs & Asphaltic")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Repairs & Asphaltic'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/repairs_json.html', q=q)})

    return render_template('projects/completed/repairs_aphaltic.html', title='Repairs & Asphaltic', repairs_list=repairs_list, posts=posts)

@completed_proj.route('/completed/periodic/preconstruction', methods=['GET', 'POST']) 
def preconstruct():
    
    precons_list = CompletedProj.query.filter_by(category="Pre-Construction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Pre-Construction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/precons_json.html', q=q)})

    return render_template('projects/completed/preconstruction.html', title='Preconstruction', precons_list=precons_list, posts=posts)

@completed_proj.route('/completed/periodic/asphalticoverlay', methods=['GET', 'POST']) 
def asphalticoverlay():
    
    overlay_list = CompletedProj.query.filter_by(category="Asphaltic Overlay")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Asphaltic Overlay'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/asphaltic_json.html', q=q)})

    return render_template('projects/completed/asphaltic_overlay.html', title='Asphaltic Overlay', overlay_list=overlay_list, posts=posts)

@completed_proj.route('/completed/periodic/upgrading', methods=['GET', 'POST']) 
def upgrading():
    
    upgrade_list = CompletedProj.query.filter_by(category="Upgrading")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Upgrading'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/upgrade_json.html', q=q)})

    return render_template('projects/completed/upgrading.html', title='Upgrading', upgrade_list=upgrade_list, posts=posts)

@completed_proj.route('/completed/periodic/decongestion', methods=['GET', 'POST']) 
def decongestion():
    
    deconges_list = CompletedProj.query.filter_by(category="Decongestion")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Decongestion'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/decongestion_json.html', q=q)})

    return render_template('projects/completed/decongestion.html', title='Decongestion', deconges_list=deconges_list, posts=posts)

@completed_proj.route('/completed/periodic/supply_inst', methods=['GET', 'POST']) 
def supply():
    
    supply_list = CompletedProj.query.filter_by(category="Supply & Installation of Materials")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Supply & Installation of Materials'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/supply_json.html', q=q)})

    return render_template('projects/completed/supply.html', title='Supply & Installation of Materials', supply_list=supply_list, posts=posts)

@completed_proj.route('/completed/periodic/partial_reconst', methods=['GET', 'POST']) 
def part_reconst():
    
    part_reconst_list = CompletedProj.query.filter_by(category="Partial Reconstruction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Partial Reconstruction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/partial_reconst_json.html', q=q)})

    return render_template('projects/completed/partial_reconst.html', title='Partial Reconstruction', part_reconst_list=part_reconst_list, posts=posts)

@completed_proj.route('/completed/periodic/grading_proj', methods=['GET', 'POST']) 
def grading():
    
    grading_list = CompletedProj.query.filter_by(category="Grading")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Grading'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/grading_json.html', q=q)})

    return render_template('projects/completed/grading.html', title='Grading', grading_list=grading_list, posts=posts)

@completed_proj.route('/completed/periodic/construction', methods=['GET', 'POST']) 
def construction():
    
    const_list = CompletedProj.query.filter_by(category="Construction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Construction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/const_json.html', q=q)})

    return render_template('projects/completed/construction.html', title='Construction', const_list=const_list, posts=posts)

@completed_proj.route('/completed/periodic/regravelling', methods=['GET', 'POST']) 
def regravelling():
    
    regrav_list = CompletedProj.query.filter_by(category="Regravelling")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Regravelling'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/regrav_json.html', q=q)})

    return render_template('projects/completed/regravelling.html', title='Regravelling', regrav_list=regrav_list, posts=posts)

@completed_proj.route('/completed/periodic/surface_dressing', methods=['GET', 'POST']) 
def surface_dressing():
    
    surf_dress_list = CompletedProj.query.filter_by(category="Surface Dressing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Surface Dressing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/surf_dress_json.html', q=q)})

    return render_template('projects/completed/surf_dressing.html', title='Surface Dressing', surf_dress_list=surf_dress_list, posts=posts)

@completed_proj.route('/completed/periodic/drainage_structures', methods=['GET', 'POST']) 
def drainage_struct():
    
    drainage_list = CompletedProj.query.filter_by(category="Drainage Structures")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Drainage Structures'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/drainage_struct_json.html', q=q)})

    return render_template('projects/completed/drainage_struct.html', title='Drainage Structures', drainage_list=drainage_list, posts=posts)

@completed_proj.route('/completed/periodic/bituminous', methods=['GET', 'POST']) 
def bituminous():
    
    bituminous_list = CompletedProj.query.filter_by(category="Bituminous Surfacing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Bituminous Surfacing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/bituminous_json.html', q=q)})

    return render_template('projects/completed/bituminous.html', title='Bituminous Surfacing', bituminous_list=bituminous_list, posts=posts)

@completed_proj.route('/completed/periodic/other_projects', methods=['GET', 'POST']) 
def other_proj():
    
    others_list = CompletedProj.query.filter_by(category="Others")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM completed_proj \
                                    WHERE category = 'Others'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/completed/other_proj_json.html', q=q)})

    return render_template('projects/completed/other_proj.html', title='Other Projects', others_list=others_list, posts=posts)

#View Rehabilitation Projects details from the database
@completed_proj.route('/completed/rehab_proj/view/<int:contract_id>/details') 
def rehab_contract(contract_id):
    rehab = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", rehab.video_link) 
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/rehab_details.html', rehab=rehab, contract_id=contract_id, posts=posts)

#View Regravelling Projects details from the database
@completed_proj.route('/completed/regrav_proj/view/<int:contract_id>/details') 
def regrav_contract(contract_id):
    regrav = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", regrav.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/regrav_details.html', regrav=regrav, contract_id=contract_id, posts=posts)

#View Asphaltic Overlay Projects details from the database
@completed_proj.route('/completed/overlay_proj/view/<int:contract_id>/details') 
def overlay_contract(contract_id):
    overlay = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", overlay.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/asphaltic_details.html', overlay=overlay, contract_id=contract_id, posts=posts)

#View Bituminous Projects details from the database
@completed_proj.route('/completed/bituminous_proj/view/<int:contract_id>/details') 
def bituminous_contract(contract_id):
    bituminous = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", bituminous.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/bituminous_details.html', bituminous=bituminous, contract_id=contract_id, posts=posts)

#View Construction Projects details from the database
@completed_proj.route('/completed/construction_proj/view/<int:contract_id>/details') 
def construction_contract(contract_id):
    construction = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", construction.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/const_details.html', construction=construction, contract_id=contract_id, posts=posts)

#View Decongestion Projects details from the database
@completed_proj.route('/completed/decongestion_proj/view/<int:contract_id>/details') 
def decongestion_contract(contract_id):
    decongestion = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", decongestion.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/decongestion_details.html', decongestion=decongestion, contract_id=contract_id, posts=posts)
#View Drainage Projects details from the database
@completed_proj.route('/completed/drainage_proj/view/<int:contract_id>/details') 
def drainage_contract(contract_id):
    drainage = CompletedProj.query.get_or_404(contract_id)
    match = re.search(r"youtube\.com/.*v=([^&]*)", drainage.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/drainage_details.html', drainage=drainage, contract_id=contract_id, posts=posts)

#View Others Projects details from the database
@completed_proj.route('/completed/others_proj/view/<int:contract_id>/details') 
def others_contract(contract_id):
    others = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", others.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/others_details.html', others=others, contract_id=contract_id, posts=posts)

#View Partial Reconstruction Projects details from the database
@completed_proj.route('/completed/partial_recons_proj/view/<int:contract_id>/details') 
def partial_recons_contract(contract_id):
    partial_recons = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", partial_recons.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/part_reconst_details.html', partial_recons=partial_recons, contract_id=contract_id, posts=posts)

#View Reconstruction Projects details from the database
@completed_proj.route('/completed/reconstruction_proj/view/<int:contract_id>/details') 
def reconstruction_contract(contract_id):
    reconstruction = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", reconstruction.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/reconstruct_details.html', reconstruction=reconstruction, contract_id=contract_id, posts=posts)

#View Resealing Projects details from the database
@completed_proj.route('/completed/resealing_proj/view/<int:contract_id>/details') 
def resealing_contract(contract_id):
    resealing = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", resealing.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/reseal_details.html', resealing=resealing, contract_id=contract_id, posts=posts)

#View Supply and Installation of Materials details from the database
@completed_proj.route('/completed/supply_proj/view/<int:contract_id>/details') 
def supply_contract(contract_id):
    supply = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", supply.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/supply_details.html', supply=supply, contract_id=contract_id, posts=posts)

#View Surface Dressing details from the database
@completed_proj.route('/completed/surf_dressing_proj/view/<int:contract_id>/details') 
def surf_dressing_contract(contract_id):
    surf_dressing = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", surf_dressing.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/surf_dressing_details.html', surf_dressing=surf_dressing, contract_id=contract_id, posts=posts)

#View Upgrading details from the database
@completed_proj.route('/completed/upgrading_proj/view/<int:contract_id>/details') 
def upgrading_contract(contract_id):
    upgrading = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", upgrading.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/upgrade_details.html', upgrading=upgrading, contract_id=contract_id, posts=posts)
#View Grading details from the database
@completed_proj.route('/completed/grading_proj/view/<int:contract_id>/details') 
def grading_contract(contract_id):
    grading = CompletedProj.query.get_or_404(contract_id) 
    match = re.search(r"youtube\.com/.*v=([^&]*)", grading.video_link)
    if match:
        contract_id = match.group(1)

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('projects/completed/grading_details.html', grading=grading, contract_id=contract_id, posts=posts)

