import csv
from guitar import Guitar

FILENAME = "../../prac7/guitars.csv"


def main():
    # Read existing guitars from the file
    guitars = []
    try:
        with open(FILENAME, "r") as in_file:
            reader = csv.reader(in_file)
            next(reader)  # Skips header if it exists
            for line in reader:
                if line:  # Ensure line is not empty
                    guitars.append(Guitar(line[0], int(line[1]), float(line[2])))
    except FileNotFoundError:
        print(f"File {FILENAME} not found. Starting with an empty list of guitars.")

    # Allow user to add new guitars
    while True:
        name = input("Name (or press Enter to finish): ")
        if name == "":
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input. Please enter numeric values for year and cost.")
            continue

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")

    # Sort guitars by year
    guitars.sort()

    # Display all guitars
    for guitar in guitars:
        print(guitar)

    # Save all guitars to the file
    with open(FILENAME, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Name", "Year", "Cost"])  # Write header
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

    print(f"{len(guitars)} guitars saved to {FILENAME}")


if __name__ == "__main__":
    main()
