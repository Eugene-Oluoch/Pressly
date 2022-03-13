#imports
import secrets,os
from PIL import Image
from flask import current_app


#Function that changes the name of the image file provided so that It can conflict with the other image files
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images/',picture_fn)
    output_size = (1200,500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn