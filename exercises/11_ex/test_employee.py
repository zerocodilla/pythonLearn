import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create a new employee."""
        self.my_employee = Employee('john', 'smith', 100000)

    def test_give_default_raise(self):
        """Test that a default raise 5000 works properly."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        """Test that a custom raise works properly."""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 110000)

    if __name__ == '__main__':
        unittest.main
