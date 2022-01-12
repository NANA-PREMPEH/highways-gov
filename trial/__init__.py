from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from elasticsearch import Elasticsearch
from flask_mail import Mail
from trial.config import Config

from flask_s3 import FlaskS3






 


#Create a database Instance 
mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate() 
login_manager = LoginManager() 
login_manager.login_view = 'users.login' 
login_manager.login_message_category = 'info' 
s3 = FlaskS3()



def create_app(config_class=Config):
    #Initialise flask
    app = Flask(__name__)
    app.config.from_object(Config)

    
    #Extensions Initialization
    mail.init_app(app) 
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db) 
    s3.init_app(app)


    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
   
    #Import the blueprint objects and register with our routes
    from trial.users.routes import users
    from trial.blogs.routes import blogs
    from trial.generalforms.routes import generalforms 
    from trial.projects.routes import projects
    from trial.main.routes import main
    from trial.errors.handlers import errors
    from trial.admin.routes import admin
    from trial.leavemgt.routes import leavemgt
    from trial.ongoing_proj.routes import ongoing_proj 
    from trial.completed_proj.routes import completed_proj

    #Register the blueprint
    app.register_blueprint(users)
    app.register_blueprint(blogs)
    app.register_blueprint(generalforms)
    app.register_blueprint(projects)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(admin)
    app.register_blueprint(leavemgt)
    app.register_blueprint(ongoing_proj)
    app.register_blueprint(completed_proj)

    return app