from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask_login import UserMixin
from trial import db, login_manager, app


#Function to reload user from user id stored in session
#Decorate the function so that the extension can easily know 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Create Registration Form
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    posts = db.relationship('Leave', backref='author', lazy=True)

    #Create methods that make it easy to create tokens
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        #Return a token created by the dumps
        return s.dumps({'user_id': self.id}).decode('utf-8')

    #Create a method that verifies a token
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        #Check for expired token using a try-catch(exception) block
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#Create Leave Form Model
class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    rank = db.Column(db.String(40), nullable=False)
    section = db.Column(db.String(40), nullable=False) 
    date_app = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    tele_no = db.Column(db.Integer, nullable=False)
    leave_cat = db.Column(db.String(30), nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    supp_info = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    days_proceed = db.Column(db.Integer, nullable=False)
    effec_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    resump_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    outs_days = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

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