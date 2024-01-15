#!/usr/bin/python3
import unittest
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        """Test the attributes of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_inheritance(self):
        """Test if the User class inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes_default_values(self):
        """Test if the default values of User attributes are set correctly."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
