import os
from flask import current_app
import secrets

from trial import azure_storage
from azure.storage.blob import ContentSettings


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
   

    #Store in azure blob
    azure_storage.block_blob_service.create_blob_from_path(container_name='static/assets/static/blog_images', blob_name=photo_name, file_path=photo_path, content_settings=ContentSettings(content_type='image'))

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


    #Store in azure blob
    azure_storage.block_blob_service.create_blob_from_path(container_name='static/assets/static/profile_pics', blob_name=picture_fn, file_path=picture_path, content_settings=ContentSettings(content_type='image'))

    return picture_fn

def save_proj_image(form_picture):
    #Randomize the name of the picture(to prevent collision with other image with the same name)
    random_hex = secrets.token_hex(8)
    #Grab the file extension
    _, f_ext = os.path.splitext(form_picture.filename)      #Use of underscore to discard the filename 
    #Combine the random_hex and the file extension to get the new filename of image
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/completed_proj', picture_fn) 

    form_picture.save(picture_path)


    #Store in azure blob
    azure_storage.block_blob_service.create_blob_from_path(container_name='static/assets/static/completed_proj', blob_name=picture_fn, file_path=picture_path, content_settings=ContentSettings(content_type='image'))

    return picture_fn

def save_gallery_image(form_picture):
    #Randomize the name of the picture(to prevent collision with other image with the same name)
    random_hex = secrets.token_hex(8)
    #Grab the file extension
    _, f_ext = os.path.splitext(form_picture.filename)      #Use of underscore to discard the filename 
    #Combine the random_hex and the file extension to get the new filename of image
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/gallery', picture_fn) 

    form_picture.save(picture_path)

    #Store in azure blob
    azure_storage.block_blob_service.create_blob_from_path(container_name='static/assets/static/gallery', blob_name=picture_fn, file_path=picture_path, content_settings=ContentSettings(content_type='image'))

    return picture_fn

