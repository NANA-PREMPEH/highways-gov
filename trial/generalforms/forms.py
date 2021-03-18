from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField, RadioField, HiddenField
from wtforms.validators import DataRequired, Length, Email

#Create Leave Form
class LeaveForm(FlaskForm):
    rank = StringField('Rank', validators=[DataRequired(), Length(min=2, max=50)])
    section = StringField('Section', validators=[DataRequired(), Length(min=2, max=50)])
    date_app = StringField('Date', validators=[DataRequired()])
    tele_no = IntegerField('Telephone No', validators=[DataRequired(message="Please enter a valid mobile number")])
    leave_cat = SelectField('Leave Category', validators=[DataRequired(message="Please Choose a Category")], choices=[('', 'Please Select an Option'),
                            ('Annual/Part Leave', 'Annual/Part Leave'),('Casual Leave', 'Casual Leave'),
                            ('Maternity Leave', 'Maternity Leave'),('Sick Leave', 'Sick Leave'),
                            ('Compassionate Leave', 'Compassionate Leave'),('Study Leave', 'Study Leave'),
                            ('Examination Leave', 'Examination Leave'),('Resettlement Leave', 'Resettlement Leave')])
    no_of_days = IntegerField('No. of Days/Months ', validators=[DataRequired(message="Please enter a valid number")]) 
    start_date = StringField('From:', validators=[DataRequired()])
    end_date = StringField('To:', validators=[DataRequired()])
    supp_info = TextAreaField('Supplementary Information', validators=[DataRequired(), Length(min=2)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = IntegerField('Mobile No', validators=[DataRequired(message="Please enter a valid mobile number")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    days_proceed = IntegerField('Days to proceed', validators=[DataRequired(message="Please enter a valid number")])
    effec_date = StringField('Effective Date of Leave', validators=[DataRequired()])
    resump_date = StringField('Date of Resumption', validators=[DataRequired()])
    outs_days = IntegerField('Outstanding Leave Day(s)', validators=[DataRequired(message="Please enter a valid number")])
    leavestatus = HiddenField('Leave Status', default = 'Pending')
    submit = SubmitField('Submit & Preview') 


#Create a Defect Report Form
class DefectReportForm(FlaskForm):
    report = RadioField('label', validators=[DataRequired(message="Please")], choices=[('report', 'report /'), ('complain', 'complain')])
    road_desc = StringField('Road', validators=[DataRequired(), Length(min=2, max=50)])
    dist_desc = StringField('District', validators=[DataRequired(), Length(min=2, max=50)])
    reg_desc = StringField('Region', validators=[DataRequired(), Length(min=2, max=50)])
    direction = StringField('Direction', validators=[DataRequired(), Length(min=2, max=50)])
    details = TextAreaField('', validators=[DataRequired(), Length(min=2)])
    name_desc = StringField('Name:', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = IntegerField('Telephone No: ', validators=[DataRequired(message="Please enter a valid mobile number")])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    date = StringField('Date:', validators=[DataRequired()])
    submit = SubmitField('Submit')

