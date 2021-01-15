import os

basedir = os.path.abspath(os.path.dirname(__file__))
#Set the configurations
class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('JAWSDB_URL')
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'static/blog_images')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    GHA_ADMIN = os.environ.get('GHA_ADMIN')

    
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 3
    

