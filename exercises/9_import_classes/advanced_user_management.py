from user_management import User


class Privileges:
    """List the administrator's set of privileges."""
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        """Print privileges of admin user."""
        print("\nAdmin user has the following privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """Represents superuser info for admin."""

    def __init__(self, first_name, last_name, age, location, login_attempts):
        """
        Initialize attributes of a parent class.
        Then initialize attributes of admin user.
        """
        super().__init__(first_name, last_name, age, location, login_attempts)
        self.privileges = Privileges()
