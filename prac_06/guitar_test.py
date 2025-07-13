"""
CP1404/CP5632 Practical
Basic manual tests for Guitar class
"""
from guitar import Guitar


def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    # Test get_age()
    print(f"{guitar.name} get_age() - Expected {2025 - 1922}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {2025 - 2012}. Got {other.get_age()}")

    # Test is_vintage()
    print()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


# Call the run_tests() function here, outside of any function definitions.
run_tests()
