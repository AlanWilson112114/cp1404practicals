import datetime


class Project:
    """Represents a project with essential details."""

    def __init__(self, name, start_date, priority, estimated_cost, completion_percentage):
        """Initializes a Project object with the given attributes."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.estimated_cost = float(estimated_cost.replace('$', '').replace(',', ''))
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """Returns a string representation of the Project object."""
        return (f"{self.name}, starting on: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"cost estimate: ${self.estimated_cost:,.2f}, completion: {self.completion_percentage}%")

    def to_line(self):
        """Converts the Project object to a tab-delimited string for file storage"""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t"
                f"${self.estimated_cost:,.2f}\t{self.completion_percentage}")

    def is_complete(self):
        """Checks if the project is finished (100% completion)."""
        return self.completion_percentage == 100
