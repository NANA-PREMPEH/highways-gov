from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FloatField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from trial.models import User
from flask_login import current_user 



#Create Registration Form
class RegistrationForm(FlaskForm):
    ref_no = StringField('Ref. No', validators=[DataRequired()])
    acc_gen = StringField('Acc-Gen Staff No.', validators=[DataRequired()])
    ssf = StringField('Ssf No.', validators=[DataRequired()]) 
    name = StringField('Full Name', validators=[DataRequired()])
    dob = StringField('Birth Date', validators=[DataRequired()]) 
    
    sex = SelectField('Sex', validators=[DataRequired(message="Please Choose a Category")],
                                    choices=[('', 'Choose'), ('M', 'M'), ('F', 'F')])
    job_pos = StringField('Job Position', validators=[DataRequired()])
    date_engaged = StringField('Date Engaged', validators=[DataRequired()])
    pres_appt = StringField('Pres. Appt', validators=[DataRequired()])
    division = StringField('Division/Station', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
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

#Create Registration Form
class UpdateStaffForm(FlaskForm):
    ref_no = StringField('Ref. No', validators=[DataRequired()])
    acc_gen = StringField('Acc-Gen Staff No.', validators=[DataRequired()])
    ssf = StringField('Ssf No.', validators=[DataRequired()])
    name = StringField('Full Name', validators=[DataRequired()])
    dob = StringField('Birth Date', validators=[DataRequired()]) 
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    sex = SelectField('Sex', validators=[DataRequired(message="Please Choose a Category")],
                                    choices=[('', 'Choose'), ('M', 'M'), ('F', 'F')])
    job_pos = StringField('Job Position', validators=[DataRequired()])
    date_engaged = StringField('Date Engaged', validators=[DataRequired()])
    pres_appt = StringField('Pres. Appt', validators=[DataRequired()])
    division = StringField('Division/Station', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()]) 
    submit = SubmitField('Update Details')

    #Check to see if username already exists
    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('Name already exists. Please choose a different one.')


    #Check to see if email already exists
    #def validate_email(self, email):
        #all_email = []
        #staff = User.query.all()
        #for prs in staff:
          #  s_email = prs.email
           # all_email.append(s_email)
        #if email.data != staff.email:
         #   user = User.query.filter_by(email=email.data).first()
           # if user:
                #raise ValidationError('Email already exists. Please choose a different one.')


#Create Blog Post Form
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    blog_content = TextAreaField('Content', validators=[DataRequired()]) 
    picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Post')

#Create Blog Post Form
class GalleryForm(FlaskForm):
    picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit')

#Create Completed Projects Form
class CompletedProjectsForm(FlaskForm):
    region = StringField('Region', validators=[DataRequired()])
    project = StringField('Project', validators=[DataRequired()])
    length = StringField('Length (Km)')
    contractor = StringField('Contractor', validators=[DataRequired()])
    category = StringField('Category')
    date_commenced = StringField('Date of Commence')
    date_completed = StringField('Date of Completion')
    pic_one = FileField('Upload Image 1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    pic_two = FileField('Upload Image 2', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    contract_sum = StringField('Original Contract Sum')
    amt_to_date = StringField('Total Amount Cert. To Date')
    video_title = StringField('Video Title')
    video_link = StringField('Video Link', render_kw={'placeholder':"https://www.youtube.com/watch?v="})  
    video_description = TextAreaField('Video Description')
    submit = SubmitField('Submit')

#Create Ongoing Projects Form
class OngoingProjectsForm(FlaskForm):
    region = StringField('Region', validators=[DataRequired()])
    project = StringField('Project', validators=[DataRequired()])
    length = StringField('Length (Km)')
    contractor = StringField('Contractor', validators=[DataRequired()])
    category = StringField('Category')
    date_commenced = StringField('Date of Commence')
    date_completed = StringField('Date of Completion')
    revised_date = StringField('Revised Completion Date')
    contract_sum = StringField('Original Contract Sum')
    revised_sum = StringField('Revised Contract Sum')
    amt_to_date = StringField('Total Amount Cert. To Date')
    video_title = StringField('Video Title')
    video_link = StringField('Video Link', render_kw={'placeholder':"https://www.youtube.com/watch?v="})  
    video_description = TextAreaField('Video Description')
    submit = SubmitField('Submit')

#Create Terminated Projects Form
class TerminatedProjectsForm(FlaskForm):
    region = StringField('Region', validators=[DataRequired()])
    project = StringField('Project', validators=[DataRequired()])
    length = StringField('Length (Km)')
    contractor = StringField('Contractor')
    date_commenced = StringField('Date of Commence')
    date_completed = StringField('Date of Completion')
    revised_date = StringField('Revised Completion Date')
    contract_sum = StringField('Original Contract Sum')
    revised_sum = StringField('Revised Contract Sum')
    amt_to_date = StringField('Total Amount Cert. To Date')
    video_title = StringField('Video Title')
    video_link = StringField('Video Link', render_kw={'placeholder':"https://www.youtube.com/watch?v="})  
    video_description = TextAreaField('Video Description')
    submit = SubmitField('Submit')

#Create Awarded Projects Form
class AwardedProjectsForm(FlaskForm):
    region = StringField('Region', validators=[DataRequired()])
    project = StringField('Project', validators=[DataRequired()])
    length = StringField('Length (Km)')
    contractor = StringField('Contractor')
    date_commenced = StringField('Date of Commence')
    date_completed = StringField('Date of Completion')
    revised_date = StringField('Revised Completion Date')
    contract_sum = StringField('Original Contract Sum')
    revised_sum = StringField('Revised Contract Sum')
    amt_to_date = StringField('Total Amount Cert. To Date')
    cost_to_complete = StringField('Cost To Complete')
    video_title = StringField('Video Title')
    video_link = StringField('Video Link', render_kw={'placeholder':"https://www.youtube.com/watch?v="})  
    video_description = TextAreaField('Video Description')
    submit = SubmitField('Submit')

#Create Planned Projects Form
class PlannedProjectsForm(FlaskForm):
    region = StringField('Region', validators=[DataRequired()])
    project = StringField('Project', validators=[DataRequired()])
    length = StringField('Length (Km)')
    contractor = StringField('Contractor')
    category = StringField('Category')
    date_commenced = StringField('Date of Commence')
    date_completed = StringField('Date of Completion')
    revised_date = StringField('Revised Completion Date')
    contract_sum = StringField('Original Contract Sum')
    revised_sum = StringField('Revised Contract Sum')
    amt_to_date = StringField('Total Amount Cert. To Date')
    video_title = StringField('Video Title')
    video_link = StringField('Video Link', render_kw={'placeholder':"https://www.youtube.com/watch?v="})  
    video_description = TextAreaField('Video Description')
    submit = SubmitField('Submit')