from flask_wtf import FlaskForm
from flask_login import current_user
from trial.models import Staff, User
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

#Create Login Form
class LoginForm(FlaskForm):
    acc_gen = StringField('Staff No. / Email', validators=[DataRequired()])  
    password = StringField('Password', validators=[DataRequired()]) 
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

#Create UpdateAccount Form
class UpdateAccountForm(FlaskForm):
    acc_gen = StringField('Acct-Gen Staff No.', validators=[DataRequired()]) 
    dob = StringField('Date Of Birth', validators=[DataRequired()]) 
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])]) 
    submit = SubmitField('Update')

    #Check to see if username already exists
    def validate_username(self, name):
        if name.data != current_user.name:
            user = User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('Name already exists. Please choose a different one.')


    #Check to see if email already exists
    def validate_email(self, email):
        
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists. Please choose a different one.') 


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
