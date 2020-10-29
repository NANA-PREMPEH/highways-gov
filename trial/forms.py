from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, NumberRange


#Create a Defect Report Form
class DefectReportForm(FlaskForm):
    report = RadioField('label', validators=[DataRequired()], choices=[('report', 'report /'), ('complain', 'complain')])
    road_desc = StringField('Road', validators=[DataRequired(), Length(min=2, max=50)])
    dist_desc = StringField('District', validators=[DataRequired(), Length(min=2, max=50)])
    reg_desc = StringField('Region', validators=[DataRequired(), Length(min=2, max=50)])
    direction = StringField('Direction', validators=[DataRequired(), Length(min=2, max=50)])
    details = TextAreaField('', validators=[DataRequired(), Length(min=2)])
    name_desc = StringField('Name:', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = IntegerField('Telephone No: ', validators=[DataRequired(message="Please enter a valid mobile number")])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    date = DateField('Date:', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Submit')


class LeaveForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    rank = StringField('Rank', validators=[DataRequired(), Length(min=2, max=50)])
    section = StringField('Section', validators=[DataRequired(), Length(min=2, max=50)])
    date_app = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    tele_no = IntegerField('Telephone No', validators=[DataRequired(message="Please enter a valid mobile number")])
    leave_cat = SelectField('Leave Category', validators=[DataRequired(message="Please Choose a Category")], choices=[('', 'Please Select an Option'),
                            ('Annual/Part Leave', 'Annual/Part Leave'),('Casual Leave', 'Casual Leave'),
                            ('Maternity Leave', 'Maternity Leave'),('Sick Leave', 'Sick Leave'),
                            ('Compassionate Leave', 'Compassionate Leave'),('Study Leave', 'Study Leave'),
                            ('Examination Leave', 'Examination Leave'),('Resettlement Leave', 'Resettlement Leave')])
    no_of_days = IntegerField('No. of Days/Months ', validators=[DataRequired(message="Please enter a valid number")])
    start_date = DateField('From:', format='%Y-%m-%d')
    end_date = DateField('To:', format='%Y-%m-%d')
    supp_info = TextAreaField('Supplementary Information', validators=[DataRequired(), Length(min=2)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = IntegerField('Mobile No', validators=[DataRequired(message="Please enter a valid mobile number")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    days_proceed = IntegerField('Days to proceed', validators=[DataRequired(message="Please enter a valid number")])
    effec_date = DateField('Effective Date of Leave', format='%Y-%m-%d')
    resump_date = DateField('Date of Resumption', format='%Y-%m-%d')
    outs_days = IntegerField('Outstanding Leave Day(s)', validators=[DataRequired(message="Please enter a valid number")])
    submit = SubmitField('Submit & Preview')

