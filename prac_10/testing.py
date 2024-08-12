import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """
    Return the string `s`, repeated `n` times, with spaces in between each repetition.
    """
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Check if the word is as long as or longer than a specified length.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """
    Execute test cases to verify that the functions work as expected.
    """
    # Basic assertion to check if the repeat_string function works properly
    assert repeat_string("Python", 1) == "Python"

    # This test is expected to fail since the output should be "hi hi"
    assert repeat_string("hi", 2) == "hi hi"

    # Create a Car instance to test default values
    test_car = Car()
    assert test_car._odometer == 0, "Default odometer value is incorrect"
    assert test_car.fuel == 0, "Default fuel value is incorrect"

    # Create a Car instance with specified fuel and test it
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Fuel value is incorrect when passed to the constructor"


run_tests()


def format_phrase_as_sentence(sentence):
    """
    Format a phrase so that it starts with a capital letter and ends with a period.

    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('meow meow meow')
    'Meow meow meow.'
    """
    if sentence[-1] != ".":
        sentence += "."
    return sentence.capitalize()


doctest.testmod()
