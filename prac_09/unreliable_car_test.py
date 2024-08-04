from unreliable_car import UnreliableCar


def test_unreliable_car():
    """Test the UnreliableCar's drive method."""
    bad_car = UnreliableCar("Hunter's Car", 100, 50)

    # Drive the car a few times to see if it drives or not based on reliability
    for i in range(10):
        distance = bad_car.drive(10)
        print(f"Attempt {i + 1}: Distance driven: {distance} km")

    # Print the final state of the car
    print(bad_car)
