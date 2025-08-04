import sqlite3

def connect_database():
    return sqlite3.connect("C:/sqlite3 db/learning_crud.db")

def execute_query(query):
    conn = connect_database()
    c = conn.cursor()
    result = c.execute(query)
    response = result.fetchall()
    c.close()
    conn.close()
    return response

myquery = "SELECT * FROM employee"
print("RESULT IS ",execute_query(myquery))

def find_total_salary_paid():
    query = "SELECT SUM(salary) FROM employee_salary"
    return execute_query(query)

print("\nTotal Salary Paid:", find_total_salary_paid()[0][0])

def display_employee_salary_table():
    emp_sal = "SELECT * FROM employee_salary"
    return execute_query(emp_sal)

for row in display_employee_salary_table():
    print(row)


def display_highest_salary():
    query = "SELECT MAX(salary) FROM employee_salary"
    return execute_query(query)

print("\nThe highest salary is:",display_highest_salary()[0][0])

def find_total_salary_by_employee():
    query = """
        SELECT e.name,
               SUM(s.salary) AS total_salary
        FROM employee e
        JOIN employee_salary s ON e.id = s.emp_id
        GROUP BY e.name
    """
    return execute_query(query)

print("\nTotal salary per employee is:", find_total_salary_by_employee())

def find_salary_by_designation():
    query = """
        SELECT e.designation,
        AVG(s.salary) as avg_salary
        FROM employee e
        JOIN employee_salary s ON e.id = s.emp_id
        GROUP BY e.designation
"""
    return execute_query(query)

print("\nThe average salary per designation is:", find_salary_by_designation())

def max_min_salary():
    query = """
        SELECT MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
        from employee_salary;
"""
    return execute_query(query)

print("\nThe highest and lowest salaries are:",max_min_salary())


def find_salary_based_on_experience():
    query = """
        SELECT e.experience,
               AVG(s.salary) AS avg_salary
        FROM employee e
        JOIN employee_salary s ON e.id = s.emp_id
        GROUP BY e.experience
    """
    return execute_query(query)

print("\nSalary of employees based on experience:",find_salary_based_on_experience())

def employees_earning_less_than_40000():
    query = """
SELECT emp.name
FROM employee AS emp
JOIN employee_salary AS sal ON emp.id = sal.emp_id
WHERE sal.salary > (
    SELECT MIN(salary)
    FROM employee_salary
)
AND sal.salary < 40000;
"""
    return execute_query(query)

print("\nEmployees earning more than the lower limit but less than 40000:",employees_earning_less_than_40000())

def average_salary_per_month():
    query = """
        SELECT strftime('%Y-%m', salary_date) AS salary_month,
        AVG(salary) AS average_monthly_salary
        FROM employee_salary
        GROUP BY salary_month
"""
    return execute_query(query)

print("\nThe average salary per month is:", average_salary_per_month())

def employee_salary_lesser_than_average_salary():
    query = """
SELECT sal.emp_id
FROM employee_salary AS sal
WHERE sal.salary <(
SELECT AVG(salary)
FROM employee_salary
)
"""
    return execute_query(query)

print("\n Employee IDs of employees whose salaries are lesser than average salaries:", employee_salary_lesser_than_average_salary())

def active_employees_who_joined_in_july():
    query = """
SELECT * FROM employee
WHERE status = 'Active'
AND strftime('%m', joining_date) = '07';
"""

    return execute_query(query)

print("\n Active employees who joined in July:", active_employees_who_joined_in_july())

def managers_who_joined_after_april():
    query = """
SELECT * FROM employee
WHERE designation LIKE '%Manager%'
AND joining_date > '2025-04-30';
"""

    return execute_query(query) 

print("\n Managers who joined after april:",managers_who_joined_after_april())

def oldest_employees_according_to_joining_date():
    query = """
SELECT * FROM employee
ORDER BY joining_date ASC
LIMIT 2;
"""
    return execute_query(query)

print("\n The oldest employees are:", oldest_employees_according_to_joining_date())

def employees_earning_more_than_average():
    query = """
SELECT emp.name,emp.designation,sal.salary
FROM employee AS emp
JOIN employee_salary AS sal ON emp.id = sal.emp_id
WHERE sal.salary > (
  SELECT AVG(salary) FROM employee_salary
)
"""
    return execute_query(query)

print("The employees who earn more than average:", employees_earning_more_than_average())

def get_salary_range():
    query = "SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM employee_salary"
    return execute_query(query)

print("\n The employee salary range is:", get_salary_range())