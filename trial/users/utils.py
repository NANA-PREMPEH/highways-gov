import os
from flask import url_for, current_app, abort
import secrets
from functools import wraps
from PIL import Image
from trial import mail
from flask_mail import Message 
from flask_login import current_user
from trial.models import Permission
import boto3


#define a save picture function
#Takes picture data as an argument
def save_picture(form_picture):
    #Randomize the name of the picture(to prevent collision with other image with the same name)
    random_hex = secrets.token_hex(8)
    #Grab the file extension
    _, f_ext = os.path.splitext(form_picture.filename)      #Use of underscore to discard the filename 
    #Combine the random_hex eith the file extension to get the new filename of image
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn) 

    #Resize the Image submitted
    output_size = (125, 125)
    i = Image.open(form_picture)
    #Resize the Image
    i.thumbnail(output_size)
    i.save(picture_path)

    #Store in aws s3 bucket
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.Bucket('static-gha').upload_file(picture_path, 'static/profile_pics'+picture_fn, ExtraArgs={'ACL':'public-read'})

    return picture_fn
  
#Function to send reset email
def send_reset_email(user):
    token = user.get_reset_token()
    #Create email message
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f''' To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made 
'''

    #Send message
    mail.send(msg)

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
 
def admin_required(f):
    return permission_required(Permission.ADMIN)(f) 