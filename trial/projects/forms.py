from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContractDetailsForm(FlaskForm):
    name_of_contract = StringField('Name of Contract', validators=[DataRequired()])
    length = FloatField('Length (Km)', validators=[DataRequired()])
    lot = StringField('Lot', validators=[DataRequired()])
    contract_sum = StringField('Contract Sum', validators=[DataRequired()])
    contractor = StringField('Contractor', validators=[DataRequired()])
    date_commenced = StringField('Date of Commence', validators=[DataRequired()])
    date_completed = StringField('Date of Completion', validators=[DataRequired()])
    video_title = StringField('Video Title', validators=[DataRequired()])
    video_link = StringField('Video Link', validators=[DataRequired()], render_kw={'placeholder':"https://www.youtube.com/watch?v="})
    video_description = TextAreaField('Video Description')
    submit = SubmitField('Submit')