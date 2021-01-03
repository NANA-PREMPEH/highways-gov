import os
#Set the configurations
class Config:
    
    SECRET_KEY = '2c52cdd22c951b91edf8e9a683441d2f'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    GHA_ADMIN = os.environ.get('GHA_ADMIN')

    
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 3
    

