class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get age of the guitar based on the current year"""
        return 2023 - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage"""
        return self.get_age() > 50

    def __lt__(self, other):
        """Arrange by year"""
        return self.year < other.year
