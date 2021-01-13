from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class DateForm(FlaskForm):
    start_date = StringField('From :', validators=[DataRequired()])
    end_date = StringField('To :', validators=[DataRequired()])
    submit = SubmitField('Submit')