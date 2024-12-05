import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'uploads')

# Flask configuration
SECRET_KEY = "your_secret_key"
UPLOAD_FOLDER = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
JSON_DATA_PATH = os.path.join(BASE_DIR, 'data')
