import sqlite3

def connect_db():
    conn = sqlite3.connect("C:/sqlite3 db/learning_crud.db")
    conn.row_factory = sqlite3.Row
    return conn

def unassign_project(emp_id, project_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        UPDATE employee_project
        SET project_status = 'Unassigned'
        WHERE emp_id = ? AND project_id = ?
    """, (emp_id, project_id))
    conn.commit()
    conn.close()

def get_projects_with_assignments():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT p.id, p.project_name, p.customer_name
        FROM new_projects p
        JOIN employee_project ep ON p.id = ep.project_id
        WHERE ep.project_status != 'Unassigned'
    """)
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_employees_with_end_dates():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        SELECT e.id, e.name, ep.project_id, ep.end_date
        FROM employee e
        JOIN employee_project ep ON e.id = ep.emp_id
        WHERE ep.project_status != 'Unassigned'
    """)
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_completed_projects():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT p.id, p.project_name
        FROM new_projects p
        JOIN employee_project ep ON p.id = ep.project_id
        WHERE ep.project_status = 'Completed'
    """)
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]
