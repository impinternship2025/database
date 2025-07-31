from employee import (
    add_employee,
    add_emp_skill,
    find_matching_project_for_employee,
    assign_project
)

def main():
    name = input("Enter employee name: ")
    emp_id = add_employee(name)
    print(f"\nEmployee '{name}' added with ID: {emp_id}")

    skill_count = int(input("How many skills does the employee have? "))
    for i in range(skill_count):
        print(f"\nSkill {i + 1}:")
        skill = input("Enter skill: ")
        skill_type = input("Enter skill type: ")
        add_emp_skill(emp_id, skill, skill_type)

    print("\nFinding matching projects for the employee...\n")
    matches = find_matching_project_for_employee(emp_id)

    if not matches:
        print("No matching projects found for this employee.")
    else:
        print("Matching projects:")
        for i in range(len(matches)):
            project = matches[i]
            print(f"{i + 1}. {project['project_name']} (Customer: {project['customer_name']})")

        choice = int(input("\nSelect a project number to assign the employee: "))
        selected_index = choice - 1  
        selected_project_dict = matches[selected_index]  
        project_id = selected_project_dict['id'] 

        assign_project(emp_id, project_id)
        print(f"\nEmployee assigned to project: {selected_project_dict['project_name']}")

if __name__ == "__main__":
    main()
