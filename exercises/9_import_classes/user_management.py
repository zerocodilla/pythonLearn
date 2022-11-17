class User:
    """Storing info about users."""

    def __init__(self, first_name, last_name, age, location, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        """Print info about user."""
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}."
              f"\nAge: {self.age}"
              f"\nLocation: {self.location}"
              f"\nLogin attempts: {self.login_attempts}")

    def greet_user(self):
        """Greet user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self, attempt):
        """Add login attempt to login_attempts value."""
        self.login_attempts += attempt

    def reset_login_attempts(self):
        """Reset the value of login_ attempts to 0."""
        self.login_attempts = 0