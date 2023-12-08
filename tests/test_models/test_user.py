#!/usr/bin/python3
"""
Test for User Class
"""
import unittest
from datetime import datetime
from models.user import User


class UserTests(unittest.TestCase):
    """
    User test class
    """
    def test_user(self):
        """
        Ensure presence
        of essential attributes
        """
        my_instance = User()
        self.assertTrue(hasattr(my_instance, "id"))
        self.assertTrue(hasattr(my_instance, "created_at"))
        self.assertTrue(hasattr(my_instance, "updated_at"))
        self.assertTrue(hasattr(my_instance, "email"))
        self.assertTrue(hasattr(my_instance, "password"))
        self.assertTrue(hasattr(my_instance, "first_name"))
        selt.assertTrue(hasattr(my_instance, "last_name"))

        """
        Check attribute types
        """
        self.assertIsInstance(my_instance.id, str)
        self.assertIsInstance(my_instance.created_at, datetime)
        self.assertIsInstance(my_instance.updated_at, datetime)
        self.assertIsInstance(my_instance.email, str)
        self.assertIsInstance(my_instance.password, str)
        self.assertIsInstance(my_instance.first_name, str)
        self.assertIsInstance(my_instance.last_name, str)

    if __name__ == '__main__':
        unittest.main()
