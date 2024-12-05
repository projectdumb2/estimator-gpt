from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
import os
import json
from werkzeug.utils import secure_filename
from .models import Units, Projects
from .utils import allowed_file, load_json, save_json

main = Blueprint('main', __name__)

DATA_DIR = os.getenv('JSON_DATA_PATH', './data')
UNITS_FILE = os.path.join(DATA_DIR, 'units.json')
PROJECTS_FILE = os.path.join(DATA_DIR, 'projects.json')

# Home Page
@main.route("/")
def home():
    return render_template("index.html")

# Units Page
@main.route("/units", methods=["GET", "POST"])
def units():
    units = load_json(UNITS_FILE)

    if request.method == "POST":
        unit_name = request.form.get("name")
        unit_cost = float(request.form.get("cost", 0))
        unit_type = request.form.get("type")
        average_income = float(request.form.get("income", 0)) if unit_type == "income" else None

        if not unit_name or not unit_type:
            flash("All fields are required!", "error")
        else:
            new_unit = {
                "id": len(units) + 1,
                "name": unit_name,
                "cost": unit_cost,
                "type": unit_type,
                "income": average_income,
            }
            units.append(new_unit)
            save_json(UNITS_FILE, units)
            flash("Unit added successfully!", "success")
            return redirect(url_for("main.units"))

    return render_template("units.html", units=units)

# Projects Page
@main.route("/projects", methods=["GET", "POST"])
def projects():
    units = load_json(UNITS_FILE)
    projects = load_json(PROJECTS_FILE)

    if request.method == "POST":
        project_name = request.form.get("name")
        homes_passed = int(request.form.get("homes_passed", 0))
        current_customers = int(request.form.get("current_customers", 0))
        notes = request.form.get("notes")

        # Handle file upload
        file = request.files.get("image")
        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(request.app.config["UPLOAD_FOLDER"], filename)
            file.save(upload_path)

        project = {
            "id": len(projects) + 1,
            "name": project_name,
            "homes_passed": homes_passed,
            "current_customers": current_customers,
            "notes": notes,
            "image": filename,
            "units_used": [],
        }
        projects.append(project)
        save_json(PROJECTS_FILE, projects)
        flash("Project added successfully!", "success")
        return redirect(url_for("main.projects"))

    return render_template("projects.html", units=units, projects=projects)

# Summary Page
@main.route("/summary/<int:project_id>")
def summary(project_id):
    units = load_json(UNITS_FILE)
    projects = load_json(PROJECTS_FILE)
    project = next((p for p in projects if p["id"] == project_id), None)

    if not project:
        flash("Project not found!", "error")
        return redirect(url_for("main.projects"))

    total_cost = 0
    unit_breakdown = []
    for unit in project["units_used"]:
        unit_details = next((u for u in units if u["id"] == unit["id"]), {})
        unit_cost = unit_details.get("cost", 0) * unit["quantity"]
        total_cost += unit_cost
        unit_breakdown.append({
            "name": unit_details.get("name"),
            "quantity": unit["quantity"],
            "cost": unit_details.get("cost"),
            "total_cost": unit_cost
        })

    cost_per_home = total_cost / project["homes_passed"] if project["homes_passed"] > 0 else 0
    cost_per_customer = total_cost / project["current_customers"] if project["current_customers"] > 0 else 0
    average_income = sum(u["income"] for u in units if u["type"] == "income")
    roi = (average_income * project["current_customers"] * 12) / total_cost if total_cost > 0 else 0

    return render_template(
        "summary.html",
        project=project,
        unit_breakdown=unit_breakdown,
        total_cost=total_cost,
        cost_per_home=cost_per_home,
        cost_per_customer=cost_per_customer,
        roi=roi,
    )
