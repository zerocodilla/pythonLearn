# doesn't work, on hold

import unittest
#from check_user import greet_user

class GreetTestCase(unittest.TestCase):
    """Tests for '10.12_check_user.py'."""

    def test_greet_file_not_exist(self):
        """Do we ask for username if file doesn't exist?"""
        displayed_text = greet_user()
        self.assertEqual(displayed_text, "What's your name?")

    if __name__ == '__main__':
        unittest.main()
