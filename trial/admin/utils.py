import os
from flask import current_app
import secrets


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

    return photo_name 