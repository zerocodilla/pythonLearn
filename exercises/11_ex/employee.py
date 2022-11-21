class Employee:
    """Represent employee."""

    def __init__(self, first, last, annual_salary):
        """Store info about employee."""
        self.first = first.title()
        self.last = last.title()
        self.annual_salary = annual_salary

    def give_raise(self, addition=5000):
        """Add a raise to the annual salary."""
        self.annual_salary += addition


my_employee = Employee('john', 'smith', 100000)
my_employee.give_raise()
print(f"{my_employee.annual_salary}")
print(f"{my_employee.first}")


