import os
from flask import url_for, current_app
def add_cv(cv,username):
    filename = cv.filename
    print(filename)
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' +ext_type
    
    filepath = os.path.join(current_app.root_path, 'static//cv', storage_filename)
    with open(filepath, 'wb') as f:
        cv.save(f)
    return storage_filename