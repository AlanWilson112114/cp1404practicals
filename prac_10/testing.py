import doctest
from car import Car


def repeat_string(s, n):
    """Return the string `s`, repeated `n` times, with spaces between each repetition."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """Return True if `word` length is at least `length`.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run basic tests for the functions and Car defaults."""
    # Basic assertion to check if the repeat_string function works properly
    assert repeat_string("Python", 1) == "Python"

    # This should pass: repeating 'hi' twice yields 'hi hi'
    assert repeat_string("hi", 2) == "hi hi"

    # Create a Car instance to test default values
    test_car = Car()
    assert test_car._odometer == 0, "Default odometer value is incorrect"
    assert test_car.fuel == 0, "Default fuel value is incorrect"

    # Create a Car instance with specified fuel and test it
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Fuel value is incorrect when passed to the constructor"

    # Another test for fuel setting
    another_car = Car(fuel=50)
    assert another_car.fuel == 50, "Fuel value is incorrect for another car"


def format_phrase_as_sentence(sentence):
    """Format a phrase so it starts with a capital letter and ends with a single full stop.

    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('meow meow meow')
    'Meow meow meow.'
    """
    if not sentence:
        return "."
    if sentence[-1] != ".":
        sentence += "."
    return sentence[0].upper() + sentence[1:]


if __name__ == "__main__":
    run_tests()
    doctest.runmod()
