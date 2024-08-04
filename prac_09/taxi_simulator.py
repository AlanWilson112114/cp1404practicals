from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU_STRING = """
    q)uit, c)hoose taxi, d)rive
    >>> """


def main():
    """Taxi simulator using Taxi and SilverServiceTaxi classes."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print(f"Bill to date: ${bill:.2f}")
    choice = input(MENU_STRING).lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == 'd':
            bill = drive_taxi(current_taxi, bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        choice = input(MENU_STRING).lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi, bill):
    """Drive the selected Taxi and update the bill."""
    if not current_taxi:
        print("You need to choose a taxi before you can drive")
    else:
        try:
            distance = int(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            bill += trip_cost
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        except ValueError:
            print("Invalid distance")
    return bill


def choose_taxi(taxis, current_taxi):
    """Choose a Taxi from the list."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            current_taxi = taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Not a valid number")
    return current_taxi


if __name__ == "__main__":
    main()
