"""
CP1404/CP5632 Practical
Guitar program.
"""
from guitar import Guitar


def main():
    """Main program to manage and display a list of guitars."""
    guitars = []

    print("My guitars!")

    # Input loop: ask the user for guitar details until they enter a blank name
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitars.append(Guitar(name, year, cost))  # Store new Guitar object
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    # Add sample guitars for testing convenience
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    # Display the guitars with index and vintage tag if applicable
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):  # Use 1-based indexing
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
