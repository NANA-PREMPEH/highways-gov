from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField


class LeaveAction(FlaskForm):

    approve = HiddenField('approve')
    cancel = HiddenField('cancel')
    reject = HiddenField('reject')
    id = HiddenField('')
    confirm = SubmitField('Confirm')

