from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email


#Create a Defect Form
class DefectForm(FlaskForm):
    report = RadioField('label', choices=[('report', 'report /'), ('complain', 'complain')])
    road_desc = StringField('Road', validators=[DataRequired(), Length(min=2, max=50)])
    dist_desc = StringField('District', validators=[DataRequired(), Length(min=2, max=50)])
    reg_desc = StringField('Region', validators=[DataRequired(), Length(min=2, max=50)])
    direction = StringField('Direction', validators=[DataRequired(), Length(min=2, max=50)])
    details = TextAreaField('', validators=[DataRequired()])
    name_desc = StringField('Name:', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = IntegerField('Telephone No: ', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    date = DateField('Date:', validators=[DataRequired()], format='%Y-%m-%d')


#Create Leave Form
class LeaveForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    rank = StringField('Rank', validators=[DataRequired(), Length(min=2, max=50)])
    section = StringField('section', validators=[DataRequired(), Length(min=2, max=50)])
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    tel_no = IntegerField('Telephone No', validators=[DataRequired()])
    no_of_days = IntegerField('No. of Days/Months ', validators=[DataRequired()])
    start_date = DateField('From:', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('To:', validators=[DataRequired()], format='%Y-%m-%d')
    supp_info = TextAreaField('Supplementary Information', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = IntegerField('Mobile No', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    days_proceed = IntegerField('Days to proceed', validators=[DataRequired()])
    effec_date = DateField('Effective Date of Leave', validators=[DataRequired()], format='%Y-%m-%d')
    resump_date = DateField('Date of Resumption', validators=[DataRequired()], format='%Y-%m-%d')
    outs_days = IntegerField('Outstanding Leave Day(s)', validators=[DataRequired()])
    leave_cat = SelectField('Leave Category', validators=[DataRequired()],
                            choices=[('', 'Please Select an Option'), ('Annual/Part Leave', 'Annual/Part Leave'),
                            ('Casual Leave', 'Casual Leave'), ('Maternity Leave', 'Maternity Leave'),
                            ('Sick Leave', 'Sick Leave'), ('Compassionate Leave', 'Compassionate Leave'),
                            ('Study Leave', 'Study Leave'), ('Examination Leave', 'Examination Leave'),
                            ('Resettlement Leave', 'Resettlement Leave')])