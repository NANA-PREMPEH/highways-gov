from flask_wtf import FlaskForm
from wtforms import SubmitField 

class DateForm(FlaskForm):
    submit = SubmitField('Submit')