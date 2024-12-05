# Fiber Project Cost Estimator

A lightweight web application for estimating the costs of fiber project areas. This tool allows you to manage units, estimate project costs, and calculate return on investment (ROI) for fiber deployment projects. Data is stored in JSON files for simplicity and persistence, requiring no additional database setup.

---

## **Features**
- **Unit Management:**
  - Add and edit units with associated costs (per each, per foot, or per hour).
  - Define average income per customer for ROI calculations.

- **Project Estimation:**
  - Add project areas with a name, image, notes, total homes passed, and current customers.
  - Attach units to projects and specify their usage (quantity, feet, or hours).

- **Project Summary:**
  - Printable summary page with project details, unit breakdown, total costs, and ROI.
  - Cost per home (for 100% adoption) and cost per current customer.
  - Current take rate and ROI visualizations.

---

## **Installation**

### **Prerequisites**
1. Ubuntu server (or compatible Linux system).
2. Python 3.8+ installed.
3. Internet connection to install Python packages.

---

### **Steps**

1. **Install System Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv -y
   ```
2. **Clone The Repository**
  ```bash
  git clone <repository-url> fiber-estimator
  cd fiber-estimator
  ```

4. **Set Up a Python Virtual Environment**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

5. **Install Python Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

6. **Create Necessary Directories**
  ```bash
  mkdir -p app/static/uploads
  mkdir -p data
  chmod -R 755 app/static/uploads
  ```

7. **Initialize Data Files**
  ```bash
  echo "[]" > data/units.json
  echo "[]" > data/projects.json
  ```

8. **Run The Application**
  ```bash
  python run.py
  ```

9. **Access The Application**
  ```bash
   http://<server-ip>:5000
  ```
