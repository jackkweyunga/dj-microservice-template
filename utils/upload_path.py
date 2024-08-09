import os
from uuid import uuid4

def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = uuid4().hex + '.' + ext
    return os.path.join("images", str(instance.id), unique_filename)
