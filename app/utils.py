import os
import json

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {"png", "jpg", "jpeg", "gif"}

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
