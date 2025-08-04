import sqlite3


def connect_database():
    conn = sqlite3.connect("C:/sqlite3 db/learning_crud.db")
    conn.row_factory = sqlite3.Row  # This makes each row behave like a dict
    return conn


def execute_query(query):
    conn = connect_database()
    c = conn.cursor()
    result = c.execute(query)
    rows = result.fetchall()
    # Convert sqlite3.Row objects to dictionaries
    response = None
    if len(rows) > 0:
        response = [dict(row) for row in rows]
    c.close()
    conn.close()
    return response


def get_employees_matching_project_skills():
    query = """
    SELECT DISTINCT e.name, es.skill
    FROM employee e
    JOIN employee_skills es ON e.id = es.emp_id
    JOIN new_projects_skills_required psr ON es.skill = psr.skill
    JOIN new_projects p ON p.id = psr.project_id
    WHERE p.project_name = 'Mobile Banking App'
    """
    return execute_query(query)

print("1. Employees and their matching skills for 'Mobile Banking App':")
for row in get_employees_matching_project_skills():
    print("The employees and matching skills are:",row)
    #print(f"- {row[0]} has skill: {row[1]}")



def get_all_project_skillsets():
    query = """
    SELECT p.project_name, psr.skill
    FROM new_projects p
    JOIN new_projects_skills_required psr ON p.id = psr.project_id
    ORDER BY p.project_name
    """
    return execute_query(query)

print("\n2. Skills required for each project:")
for row in get_all_project_skillsets():
    print("Skills required for each project:",row)
    #print(f"- {row[0]} requires: {row[1]}")



def get_all_employee_skills():
    query = """
    SELECT e.name, es.skill
    FROM employee e
    JOIN employee_skills es ON e.id = es.emp_id
    ORDER BY e.name
    """
    return execute_query(query)

print("\n3. Skills of each employee:")
for row in get_all_employee_skills():
    print("Skills of each employee:",row)
    #print(f"- {row[0]} has skill: {row[1]}")



def get_skill_employee_mapping():
    query = """
    SELECT es.skill, e.name
    FROM employee_skills es
    JOIN employee e ON es.emp_id = e.id
    ORDER BY es.skill
    """
    return execute_query(query)

print("\n4. Skills and the employees who have them:")
for row in get_skill_employee_mapping():
    print("Skills and the employees who have them:",row)
    #print(f"- Skill: {row[0]} — Employee: {row[1]}")
