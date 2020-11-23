import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

#Initialise flask
app = Flask(__name__)

#Set Secret Key
app.config['SECRET_KEY'] = '2c52cdd22c951b91edf8e9a683441d2f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/newdb'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
#Initialize mail extension
mail = Mail(app)


#Create a database Instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


#Call the routes app
from trial import routes