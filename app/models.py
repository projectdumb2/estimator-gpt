import json
import os

class Units:
    @staticmethod
    def load_units(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    @staticmethod
    def save_units(file_path, units):
        with open(file_path, "w") as f:
            json.dump(units, f, indent=4)

class Projects:
    @staticmethod
    def load_projects(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    @staticmethod
    def save_projects(file_path, projects):
        with open(file_path, "w") as f:
            json.dump(projects, f, indent=4)
