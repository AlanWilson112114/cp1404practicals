class Guitar:
    """A class to represent a Guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with a name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the guitar's age."""
        return 2024 - self.year

    def is_vintage(self):
        """Check if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50
