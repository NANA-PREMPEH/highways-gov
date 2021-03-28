import os
from flask import current_app
import secrets
from PIL import Image
import boto3


#Takes picture data as an argument
def save_photo(photo):
    #Randomize the name of the picture(to prevent collision with other image with the same name)
    random_hex = secrets.token_hex(8)
    #Grab the file extension
    _, f_ext = os.path.splitext(photo.filename)      #Use of underscore to discard the filename
    #Combine the random_hex eith the file extension to get the new filename of image
    photo_name = random_hex + f_ext
    photo_path = os.path.join(current_app.root_path, 'static/blog_images', photo_name)

    photo.save(photo_path)
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.Bucket('santa-gha').upload_file(photo_path, 'static/blog_images/'+photo_name, ExtraArgs={'ACL':'public-read'})

    return photo_name 

#define a save picture function
#Takes picture data as an argument
def save_picture(form_picture):
    #Randomize the name of the picture(to prevent collision with other image with the same name)
    random_hex = secrets.token_hex(8)
    #Grab the file extension
    _, f_ext = os.path.splitext(form_picture.filename)      #Use of underscore to discard the filename 
    #Combine the random_hex and the file extension to get the new filename of image
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn) 

    form_picture.save(picture_path)


    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.Bucket('santa-gha').upload_file(picture_path, 'static/profile_pics/'+picture_fn, ExtraArgs={'ACL':'public-read'})

    return picture_fn

