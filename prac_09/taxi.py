from car import Car


class Taxi(Car):
    """A specialized type of Car that calculates taxi fares."""

    def __init__(self, name, fuel):
        """Initialize a Taxi object using the Car class's initialization."""
        super().__init__(name, fuel)
        self.price_per_km = 1.23
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation including the current fare distance and price per kilometer."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Calculate and return the total fare based on distance traveled."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Reset the fare distance to start a new fare calculation."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the car while updating the fare distance based on the traveled distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
