from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Initialise flask
app = Flask(__name__)

#Set Secret Key
app.config['SECRET_KEY'] = '2c52cdd22c951b91edf8e9a683441d2f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Create a database Instance
db = SQLAlchemy(app)

#Call the routes app
from trial import routes