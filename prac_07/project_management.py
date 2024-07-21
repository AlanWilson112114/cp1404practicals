"""
CP1404 Practical 07 - Alan Wilson
Time estimate: 2 hours
Actual Time: >2 hours
"""

import datetime
from project import Project

FILENAME = "projects.txt"

MENU_PROMPT = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>>"""


def main():
    """Main function to manage projects through a text-based menu."""
    projects = load_projects()
    choice = input(MENU_PROMPT).lower()
    while choice != "q":
        if choice == "l":  # Load projects
            projects = load_projects()
        elif choice == "s":  # Save projects
            save_projects(projects)
        elif choice == "d":  # Display projects
            show_projects(projects)
        elif choice == "f":  # Filter projects by date
            filter_projects_by_date(projects)
        elif choice == "a":  # Add a new project
            projects.append(create_new_project())
        elif choice == "u":  # Update an existing project
            update_existing_project(projects)
        else:
            print("Invalid option. Please try again.")
        choice = input(MENU_PROMPT).lower()

    if input("Would you like to save changes to projects.txt? (yes/no): ").strip().lower() == 'yes':
        save_projects(projects)
    print("Thank you for using the project management system.")


def load_projects():
    """Reads project data from a file and returns a list of Project objects."""
    projects = []
    try:
        with open(FILENAME, "r") as file:
            file.readline()  # Skip header line
            for line in file:
                parts = line.strip().split('\t')
                projects.append(Project(*parts))
    except FileNotFoundError:
        print(f"File not found: {FILENAME}")
    return projects


def save_projects(projects):
    """Writes the list of Project objects to a file."""
    with open(FILENAME, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_line() + '\n')


def show_projects(projects):
    """Displays projects categorized by their completion status."""
    incomplete_projects = sorted(
        (project for project in projects if not project.is_complete()),
        key=lambda p: p.priority
    )
    complete_projects = sorted(
        (project for project in projects if project.is_complete()),
        key=lambda p: p.priority
    )

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project}")


def create_new_project():
    """Prompts user for details to create and return a new Project object."""
    name = input("Enter the project name: ")
    start_date = input("Enter the start date (dd/mm/yyyy): ")
    priority = input("Enter the priority: ")
    estimated_cost = input("Enter the cost estimate: $")
    completion_percentage = input("Enter the completion percentage: ")
    return Project(name, start_date, priority, estimated_cost, completion_percentage)


def update_existing_project(projects):
    """Updates the details of an existing project based on user input."""
    for index, project in enumerate(projects):
        print(f"{index}: {project}")

    index = int(input("Select the project number to update: "))
    if 0 <= index < len(projects):
        project = projects[index]
        print(f"Current details: {project}")

        new_completion = input("Enter new completion percentage (leave blank to keep current): ")
        if new_completion:
            while not (0 <= int(new_completion) <= 100):
                print("Invalid percentage. Must be between 0 and 100.")
                new_completion = input("Enter new completion percentage: ")
            project.completion_percentage = int(new_completion)

        new_priority = input("Enter new priority (leave blank to keep current): ")
        if new_priority:
            while not new_priority.isdigit():
                print("Invalid priority. Must be a number.")
                new_priority = input("Enter new priority: ")
            project.priority = int(new_priority)

        projects[index] = project
    else:
        print("Invalid project number.")


def filter_projects_by_date(projects):
    """Filters and displays projects starting after a specified date."""
    try:
        cutoff_date_str = input("Enter the date to filter projects by (dd/mm/yyyy): ")
        cutoff_date = datetime.datetime.strptime(cutoff_date_str, "%d/%m/%Y").date()
        filtered_projects = sorted(
            (project for project in projects if project.start_date > cutoff_date),
            key=lambda p: p.start_date
        )
        show_projects(filtered_projects)
    except ValueError:
        print("Incorrect date format. Please use dd/mm/yyyy.")


if __name__ == "__main__":
    main()
