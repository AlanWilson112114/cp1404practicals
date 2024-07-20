class ProgrammingLanguage:
    """Represent key details of a programming language"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize an instance of ProgrammingLanguage"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a formatted string of programming language details"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the language's typing is dynamic"""
        return self.typing == "Dynamic"
