from employee import (
    unassign_project,
    get_projects_with_assignments,
    get_employees_with_end_dates,
    get_completed_projects
)

def main():
    while True:
        print("\n--- Employee Project Management ---")
        print("1. Unassign a project from employee")
        print("2. View projects with assigned employees")
        print("3. View employees with end dates")
        print("4. View completed projects")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            emp_id = int(input("Enter employee ID to unassign: "))
            project_id = int(input("Enter project ID to unassign: "))
            unassign_project(emp_id, project_id)
            print("Project unassigned successfully.")

        elif choice == "2":
            projects = get_projects_with_assignments()
            if not projects:
                print("No projects with assigned employees found.")
            else:
                for p in projects:
                    print(f"Project ID: {p['id']} , Name: {p['project_name']} , Customer: {p['customer_name']}")

        elif choice == "3":
            employees = get_employees_with_end_dates()
            if not employees:
                print("No employees with end dates found.")
            else:
                for e in employees:
                    print(f"Emp ID: {e['id']} , Name: {e['name']} , Project ID: {e['project_id']} , End Date: {e['end_date']}")

        elif choice == "4":
            completed = get_completed_projects()
            if not completed:
                print("No completed projects found.")
            else:
                for p in completed:
                    print(f"Project ID: {p['id']} , Name: {p['project_name']}")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
