"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Pointer Arithmetic,Year
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()
        # All other lines are language data
        for line in in_file:
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split(',')
            # Reflection and Pointer Arithmetic are stored as strings (Yes/No) and we want Booleans
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[3] == "Yes"
            # Construct a ProgrammingLanguage object using the elements
            # Year should be an int
            language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[4]))
            # Add the language we've just constructed to the list
            languages.append(language)

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


# using_csv()
def using_csv():
    """Language file reader version using the csv module"""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Skip the header
        reader = csv.reader(in_file)
        for row in reader:
            print(row)


# using_namedtuple()
def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)
        # Language will be a new subclass of the tuple data type class
        Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
        reader = csv.reader(in_file)

        for row in reader:
            language = Language._make(row)
            print(repr(language))


# using_csv_namedtuple()
def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
    with open("languages.csv", "r", newline='') as in_file:
        in_file.readline()  # Skip the header
        for language in map(Language._make, csv.reader(in_file)):
            print(language.name, 'was released in', language.year)
            print(repr(language))


if __name__ == "__main__":
    main()
    # Uncomment the functions below to test them
