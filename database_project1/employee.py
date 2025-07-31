import sqlite3

def connect_db():
    conn = sqlite3.connect("C:/sqlite3 db/learning_crud.db")
    conn.row_factory = sqlite3.Row
    return conn

def add_employee(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO employee (name) VALUES (?)", (name,))
    conn.commit()
    emp_id = cur.lastrowid
    conn.close()
    return emp_id

def add_emp_skill(emp_id, skill, skill_type):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO employee_skills (emp_id, skill, skill_type) VALUES (?, ?, ?)", (emp_id, skill, skill_type))
    conn.commit()
    conn.close()

def find_matching_project_for_employee(emp_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT np.id, np.project_name, np.customer_name
        FROM new_projects np
        JOIN new_projects_skills_required ps ON np.id = ps.project_id
        JOIN employee_skills es ON ps.skill = es.skill
        WHERE es.emp_id = ?
        GROUP BY np.id
    """, (emp_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def assign_project(emp_id, project_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO employee_project (emp_id, project_id) VALUES (?, ?)", (emp_id, project_id))
    conn.commit()
    conn.close()
