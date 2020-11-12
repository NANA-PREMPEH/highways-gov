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
        return f"Leave('{self.name}', '{self.rank}', '{self.section}', '{self.date_app}', '{self.tele_no}', \
            '{self.leave_cat}','{self.no_of_days}','{self.start_date}','{self.end_date}','{self.supp_info}', \
            '{self.address}', '{self.mobile_no}', '{self.email}', '{self.days_proceed}', '{self.effec_date}', \
            '{self.resump_date}', '{self.outs_days}')"

#Create Upgrading Table
class Upgrading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_contract = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A')
    lot = db.Column(db.String(50), nullable=True, default='N/A')
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)

    def __repr__(self):
        return f"Upgrading('{self.name_of_contract}', '{self.length}', '{self.lot}', '{self.contract_sum}', '{self.contractor}',\
                            '{self.date_commenced}','{self.date_completed}')"


#Create Regravelling Table
class Regravelling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_contract = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A')
    lot = db.Column(db.String(50), nullable=True, default='N/A')
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)

    def __repr__(self):
        return f"Regravelling('{self.name_of_contract}', '{self.length}', '{self.lot}', '{self.contract_sum}', '{self.contractor}',\
                                '{self.date_commenced}','{self.date_completed}')"


#Create Construction Table
class Construction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_contract = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A')
    lot = db.Column(db.String(50), nullable=True, default='N/A')
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)

    def __repr__(self):
        return f"Construction('{self.name_of_contract}', '{self.length}', '{self.lot}', '{self.contract_sum}', '{self.contractor}',\
                                '{self.date_commenced}','{self.date_completed}')"


#Create Rehabilitation Table
class Rehabilitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_contract = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A')
    lot = db.Column(db.String(50), nullable=True, default='N/A')
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)

    def __repr__(self):
        return f"Rehabilitation('{self.name_of_contract}', '{self.length}', '{self.lot}', '{self.contract_sum}', '{self.contractor}',\
                                 '{self.date_commenced}','{self.date_completed}')"