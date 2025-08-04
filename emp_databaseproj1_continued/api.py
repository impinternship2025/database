from flask import Flask
from employee import (
    unassign_project,
    get_projects_with_assignments,
    get_employees_with_end_dates,
    get_completed_projects
)

app = Flask(__name__)

@app.route('/unassign_project/<emp_name>/<project_name>')
def api_unassign_project(emp_name, project_name):
    unassign_project(emp_name, project_name)
    return f"Project '{project_name} unassigned from employee '{emp_name}' successfully."

@app.route('/projects_with_assignments')
def api_projects_with_assignment():
    projects = get_projects_with_assignments()
    if not projects:
        return "No projects with assignments found."
    result = "Projects with assigned employees:\n"
    for p in projects:
         result += f"- Project ID: {p['id']} , Name: {p['project_name']} , Customer: {p['customer_name']}\n"
    return result

@app.route('/employees_with_end_dates')
def api_employees_with_end_dates():
    employees = get_employees_with_end_dates()
    if not employees:
        return  "No employees with end dates found."
    result = "Employees with end dates:\n"
    for e in employees:
        result += f"- Emp ID: {e['id']} , Name: {e['name']} , Project ID: {e['project_id']} , End Date: {e['end_date']}\n" 
    return result

@app.route('/completed_projects')
def api_completed_projects():
    completed = get_completed_projects()
    if not completed:
        return "No completed projects found."
    result = "Completed projects:\n"
    for p in completed:
        result += f"- Project ID: {p['id']}, Name: {p['project_name']}\n"
    return result

if __name__ == '__main__':
    app.run(debug=True)          