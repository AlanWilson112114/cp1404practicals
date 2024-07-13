from guitar import Guitar


def run_tests():
    """Test suite for the Guitar class."""
    # Create instances of Guitar with specific attributes
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar", 2013, 4.50)

    # Test the get_age() method
    print(f"{guitar.name} get_age() - Expected {2024 - 1922}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {2024 - 2013}. Got {another_guitar.get_age()}")

    # Test the is_vintage() method
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


# Call the run_tests() function here, outside of any function definitions
run_tests()
