from flask import Flask

#Initialise flask
app = Flask(__name__)

#Set Secret Key
app.config['SECRET_KEY'] = '2c52cdd22c951b91edf8e9a683441d2f'

#Call the routes app
from trial import routes