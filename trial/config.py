import os

#Set the configurations
class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('JAWSDB_URL')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
    ADMIN_HIGHWAYS = os.environ.get('ADMIN_HIGHWAYS')
    
    AZURE_STORAGE_ACCOUNT_NAME = os.environ.get('AZURE_STORAGE_ACCOUNT_NAME')
    AZURE_STORAGE_ACCOUNT_KEY = os.environ.get('AZURE_STORAGE_ACCOUNT_KEY')
    AZURE_STORAGE_CONTAINER_NAME = os.environ.get('AZURE_STORAGE_CONTAINER_NAME')  # make sure the container is created. Refer to the previous examples or to the Azure admin panel
    AZURE_STORAGE_VIRTUAL_FOLDER_NAME = os.environ.get('AZURE_STORAGE_VIRTUAL_FOLDER_NAME')
    AZURE_STORAGE_DOMAIN = os.environ.get('AZURE_STORAGE_DOMAIN')

    
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 3

