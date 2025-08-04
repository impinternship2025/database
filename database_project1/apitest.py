from flask import Flask
from employee import (
    add_employee,
    add_emp_skill,
    find_matching_project_for_employee,
    assign_project
)

app = Flask(__name__)

@app.route('/add_employee/<name>')
def api_add_employee(name):
    emp_id = add_employee(name)
    return f"Employee '{name}' added with ID {emp_id}"

@app.route('/add_skill/<int:emp_id>/<skill>/<skill_type>')
def api_add_skill(emp_id, skill, skill_type):
    add_emp_skill(emp_id, skill, skill_type)
    return f"Skill '{skill}' ({skill_type}) added to employee ID {emp_id}"

@app.route('/match_projects/<int:emp_id>')
def api_match_projects(emp_id):
    matches = find_matching_project_for_employee(emp_id)

    if not matches:
        return "No matching projects found for this employee."

    result = "Matching projects:\n"
    for m in matches:
        result += f"- {m['project_name']} (Customer: {m['customer_name']})\n"
    return result

@app.route('/assign_project/<int:emp_id>/<int:project_id>')
def api_assign_project(emp_id, project_id):
    assign_project(emp_id, project_id)
    return f"Project {project_id} assigned to employee {emp_id}"
