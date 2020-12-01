from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

#Create Blog Post Form
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    blog_content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')