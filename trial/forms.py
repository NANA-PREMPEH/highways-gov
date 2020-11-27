from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, RadioField, TextAreaField, IntegerField, SelectField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from trial.models import User


#Create Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


#Create Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    #Check to see if username already exists
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')


    #Check to see if email already exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose a different one.')


#Create UpdateAccount Form
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    #Check to see if username already exists
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists. Please choose a different one.')


    #Check to see if email already exists
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists. Please choose a different one.')

#Create Blog Post Form
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    blog_content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    #Check to see if email already exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account for email!. Please register first')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')



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

#Create Leave Form
class LeaveForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
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
    submit = SubmitField('Submit & Preview')

