"""
CP1404/CP5632 Practical
SilverServiceTaxi class tests
"""
from silver_service_taxi import SilverServiceTaxi

# For an 18 km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78 (yikes!)

def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()