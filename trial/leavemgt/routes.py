from flask import Blueprint, render_template, redirect, url_for, request
from trial import db
from flask_login import login_required, current_user
from trial.models import Leave, User, Staff
from trial.users.utils import admin_required
from trial.leavemgt.forms import LeaveAction
from datetime import date, datetime


leavemgt = Blueprint('leavemgt', __name__)

@leavemgt.route('/management_dashboard', methods=['GET'])
@admin_required
@login_required
def leave_dash():
    form = LeaveAction()
    all_req = Leave.query.all()
    rej_no = Leave.query.filter_by(leave_status="Rejected").count()
    app_no = Leave.query.filter_by(leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(leave_status="Pending").count()
    
    tot_req = rej_no + app_no + pending_no
    return render_template('leavemgt/leave_mgt_dash.html', all_req=all_req, form=form, 
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no, tot_req=tot_req)

@leavemgt.route('/act_on_leave/<int:leave_id>', methods=['GET', 'POST'])
@login_required
def decide_on_leave_req(leave_id):
    form = LeaveAction()
    req = Leave.query.get_or_404(leave_id)
    if form.validate_on_submit():
        if form.approve.data:
            req.leave_status = form.approve.data
        elif form.reject.data:
            req.leave_status = form.reject.data
        db.session.commit()
    return redirect(url_for('leavemgt.leave_dash')) 

#View Cancelled Requests
@leavemgt.route("/view_cancelled/requests", methods=['GET', 'POST'])
@login_required
def cancelled_req():
    form = LeaveAction()
    cancelled = Leave.query.all()
    rej_no = Leave.query.filter_by(leave_status="Rejected").count()
    app_no = Leave.query.filter_by(leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(leave_status="Pending").count()

    tot_req = rej_no + app_no + pending_no
    return render_template('leavemgt/cancelled_req.html', form=form, cancelled=cancelled, rej_no=rej_no, 
                            cancel_no=cancel_no, app_no=app_no, pending_no=pending_no,  tot_req=tot_req)

#View Rejected Requests
@leavemgt.route("/view_rejected/requests", methods=['GET', 'POST'])
@login_required
def rejected_req():
    form = LeaveAction()
    rejected = Leave.query.all()
    rej_no = Leave.query.filter_by(leave_status="Rejected").count()
    app_no = Leave.query.filter_by(leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(leave_status="Pending").count()

    tot_req = rej_no + app_no + pending_no
    return render_template('leavemgt/rejected_req.html', form=form, rejected=rejected,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no, tot_req=tot_req)

#View Approved Requests
@leavemgt.route("/view_approved/requests", methods=['GET', 'POST'])
@login_required
def approved_req():
    form = LeaveAction() 
    approved = Leave.query.all()
    rej_no = Leave.query.filter_by(leave_status="Rejected").count()
    app_no = Leave.query.filter_by(leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(leave_status="Pending").count()

    tot_req = rej_no + app_no + pending_no
    return render_template('leavemgt/approved_req.html', form=form, approved=approved,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no, tot_req=tot_req)

#View Pending Requests
@leavemgt.route("/view_pending/requests", methods=['GET', 'POST'])
@login_required
def pending_req():
    form = LeaveAction()
    pending = Leave.query.all()
    rej_no = Leave.query.filter_by(leave_status="Rejected").count()
    app_no = Leave.query.filter_by(leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(leave_status="Pending").count()

    tot_req = rej_no + app_no + pending_no
    return render_template('leavemgt/pending_req.html', form=form, pending=pending,
                            rej_no=rej_no, cancel_no=cancel_no, app_no=app_no, pending_no=pending_no, tot_req=tot_req) 



#View Pending Requests
@leavemgt.route("/view_staff_list", methods=['GET', 'POST']) 
@login_required
def view_staff():
    form = LeaveAction()
    pending = Leave.query.all()
    rej_no = Leave.query.filter_by(leave_status="Rejected").count()
    app_no = Leave.query.filter_by(leave_status="Approved").count()
    cancel_no = Leave.query.filter_by(leave_status="Cancelled").count()
    pending_no = Leave.query.filter_by(leave_status="Pending").count()
    staff_pers = User.query.all()
    today = date.today()
    
    tot_req = rej_no + app_no + pending_no
    return render_template('users/staff_list.html', form=form, pending=pending,rej_no=rej_no, cancel_no=cancel_no, 
                            app_no=app_no, pending_no=pending_no, tot_req=tot_req, staff_pers=staff_pers, today=today) 

    
    
