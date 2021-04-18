from flask import render_template, redirect, request, Blueprint, jsonify
from trial import db
from datetime import datetime
from trial.models import Post, OngoingProj
from trial.projects.forms import DateForm


ongoing_proj = Blueprint('ongoing_proj', __name__)


@ongoing_proj.route('/ongoing/periodic/rehabilitation', methods=['GET', 'POST'])
def rehabilitation():
    rehab_list = OngoingProj.query.filter_by(category="Rehabilitation")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d").strftime("%Y-%m-%d") 
        end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d").strftime("%Y-%m-%d")  

        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Rehabilitation'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/rehab_json.html', q=q)})

    return render_template('projects/ongoing/rehabilitation.html', title='Rehabilitation', rehab_list=rehab_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/resealing', methods=['GET', 'POST']) 
def resealing():
    
    reseal_list = OngoingProj.query.filter_by(category="Resealing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Resealing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/reseal_json.html', q=q)})

    return render_template('projects/ongoing/resealing.html', title='Resealing', reseal_list=reseal_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/resurfacing', methods=['GET', 'POST']) 
def resurfacing():
    
    resurface_list = OngoingProj.query.filter_by(category="Resurfacing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Resurfacing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/resurface_json.html', q=q)})

    return render_template('projects/ongoing/resurfacing.html', title='Resurfacing', resurface_list=resurface_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/repairs_asphaltic', methods=['GET', 'POST']) 
def repairs_asphaltic():
    
    repairs_list = OngoingProj.query.filter_by(category="Repairs & Asphaltic")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Repairs & Asphaltic'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/repairs_json.html', q=q)})

    return render_template('projects/ongoing/repairs_aphaltic.html', title='Repairs & Asphaltic', repairs_list=repairs_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/preconstruction', methods=['GET', 'POST']) 
def preconstruct():
    
    precons_list = OngoingProj.query.filter_by(category="Pre-Construction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Pre-Construction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/precons_json.html', q=q)})

    return render_template('projects/ongoing/preconstruction.html', title='Preconstruction', precons_list=precons_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/asphalticoverlay', methods=['GET', 'POST']) 
def asphalticoverlay():
    
    overlay_list = OngoingProj.query.filter_by(category="Asphaltic Overlay")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Asphaltic Overlay'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/asphaltic_json.html', q=q)})

    return render_template('projects/ongoing/asphaltic_overlay.html', title='Asphaltic Overlay', overlay_list=overlay_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/upgrading', methods=['GET', 'POST']) 
def upgrading():
    
    upgrade_list = OngoingProj.query.filter_by(category="Upgrading")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Upgrading'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/upgrade_json.html', q=q)})

    return render_template('projects/ongoing/upgrading.html', title='Upgrading', upgrade_list=upgrade_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/decongestion', methods=['GET', 'POST']) 
def decongestion():
    
    deconges_list = OngoingProj.query.filter_by(category="Decongestion")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Decongestion'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/decongestion_json.html', q=q)})

    return render_template('projects/ongoing/decongestion.html', title='Decongestion', deconges_list=deconges_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/supply_inst', methods=['GET', 'POST']) 
def supply():
    
    supply_list = OngoingProj.query.filter_by(category="Supply & Installation of Materials")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Supply & Installation of Materials'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/supply_json.html', q=q)})

    return render_template('projects/ongoing/supply.html', title='Supply & Installation of Materials', supply_list=supply_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/partial_reconst', methods=['GET', 'POST']) 
def part_reconst():
    
    part_reconst_list = OngoingProj.query.filter_by(category="Partial Reconstruction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Partial Reconstruction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/partial_reconst_json.html', q=q)})

    return render_template('projects/ongoing/partial_reconst.html', title='Partial Reconstruction', part_reconst_list=part_reconst_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/grading_proj', methods=['GET', 'POST']) 
def grading():
    
    grading_list = OngoingProj.query.filter_by(category="Grading")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Grading'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/grading_json.html', q=q)})

    return render_template('projects/ongoing/grading.html', title='Grading', grading_list=grading_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/construction', methods=['GET', 'POST']) 
def construction():
    
    const_list = OngoingProj.query.filter_by(category="Construction")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Construction'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/const_json.html', q=q)})

    return render_template('projects/ongoing/construction.html', title='Construction', const_list=const_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/regravelling', methods=['GET', 'POST']) 
def regravelling():
    
    regrav_list = OngoingProj.query.filter_by(category="Regravelling")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Regravelling'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/regrav_json.html', q=q)})

    return render_template('projects/ongoing/regravelling.html', title='Regravelling', regrav_list=regrav_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/surface_dressing', methods=['GET', 'POST']) 
def surface_dressing():
    
    surf_dress_list = OngoingProj.query.filter_by(category="Surface Dressing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Surface Dressing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/surf_dress_json.html', q=q)})

    return render_template('projects/ongoing/surf_dressing.html', title='Surface Dressing', surf_dress_list=surf_dress_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/drainage_structures', methods=['GET', 'POST']) 
def drainage_struct():
    
    drainage_list = OngoingProj.query.filter_by(category="Drainage Structures")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Drainage Structures'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/drainage_struct_json.html', q=q)})

    return render_template('projects/ongoing/drainage_struct.html', title='Drainage Structures', drainage_list=drainage_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/bituminous', methods=['GET', 'POST']) 
def bituminous():
    
    bituminous_list = OngoingProj.query.filter_by(category="Bituminous Surfacing")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Bituminous Surfacing'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/bituminous_json.html', q=q)})

    return render_template('projects/ongoing/bituminous.html', title='Bituminous Surfacing', bituminous_list=bituminous_list, posts=posts)

@ongoing_proj.route('/ongoing/periodic/other_projects', methods=['GET', 'POST']) 
def other_proj():
    
    others_list = OngoingProj.query.filter_by(category="Others")
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        start_date = request.form['start_date']
        end_date = request.form['end_date']  
        
        q = db.engine.execute("SELECT FORMAT((t1.col_total), 2)   As col_total \
                                    FROM (SELECT IFNULL(SUM(amt_to_date),0) As col_total FROM ongoing_proj \
                                    WHERE category = 'Others'  and date_commenced >= %s  and date_completed<= %s) t1", \
                                    (start_date, end_date)).first()

        return jsonify({'data': render_template('projects/ongoing/other_proj_json.html', q=q)})

    return render_template('projects/ongoing/other_proj.html', title='Other Projects', others_list=others_list, posts=posts)
