class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has a {self.odometer} miles on it.")

    def update_odometer(self, mileage): # change value through method
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer."""
        if miles > 0:
            self.odometer += miles
        else:
            print("Your can't roll back an odometer!")
