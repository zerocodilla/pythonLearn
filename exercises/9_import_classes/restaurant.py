
class Restaurant:
    """Model of a restaurant."""

    def __init__(self, name, cuisine_type):
        """Stores info about restaurant name and cuisine."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes restaurant."""
        print(f"The restaurant is called {self.name}"
              f"\nIt serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Notify if restaurant is open."""
        print(f"The restaurant {self.name} is open.")

    def customers_served(self):
        """Print a number of served customers."""
        print(f"The restaurant served {self.number_served} customers.")

    def set_number_served(self, number):
        """Set the number customers served."""
        self.number_served = number

    def increment_number_served(self, customers):
        """Add the given amount to the number customers served."""
        if customers > 0:
            self.number_served += customers
        else:
            print("You can't decrease the number of customers who were already served.")


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream."""

    def __init__(self, name, cuisine_type, flavors):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream.
        """
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Print flavors."""
        print("\nThe following flavors are available:")
        for flavor in self.flavors:
            print(flavor)
