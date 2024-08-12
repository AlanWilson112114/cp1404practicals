from car import Car
import random


class UnreliableCar(Car):
    """UnreliableCar class is a subclass of Car"""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car considering its reliability."""
        num = random.randint(0, 100)  # Generate a random number between 0 and 100
        if num < self.reliability:
            # Drive the car if the random number is less than reliability
            distance_driven = super().drive(distance)
        else:
            # Do not drive the car; return 0 distance
            distance_driven = 0
        return distance_driven
