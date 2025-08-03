class Band:
    """Band class containing instances of the Musician class"""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __repr__(self):
        """Represent a Band with its name and musicians."""
        musicians_string = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, new_musician):
        """Add a new member to the Band."""
        self.musicians.append(new_musician)

    def play(self):
        """Use the play method in the musician class for all members in the Band."""
        return '\n'.join(musician.play() for musician in self.musicians)
