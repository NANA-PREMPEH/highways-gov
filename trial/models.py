from datetime import datetime
#Import db
from trial import db

#Create Leave Form Model
class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    rank = db.Column(db.String(40), nullable=False)
    section = db.Column(db.String(40), nullable=False) 
    date_app = db.Column(db.DateTime(100), nullable=False, default=datetime.utcnow)
    tele_no = db.Column(db.Integer, nullable=False)
    leave_cat = db.Column(db.String(30), nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime(100), nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime(100), nullable=False, default=datetime.utcnow)
    supp_info = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    days_proceed = db.Column(db.Integer, nullable=False)
    effec_date = db.Column(db.DateTime(100), nullable=False, default=datetime.utcnow)
    resump_date = db.Column(db.DateTime(100), nullable=False, default=datetime.utcnow)
    outs_days = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.rank}', '{self.section}', '{self.leave_cat}', '{self.address}')"
