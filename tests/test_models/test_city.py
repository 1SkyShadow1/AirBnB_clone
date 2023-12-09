#!/usr/bin/python3
""" unit test for city """
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for city test"""

    def test_city(self):
        """existence"""
        new = City()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasaatr(new, "updated_at"))
        self.assertTrue(hasaatr(new, "state_id"))
        self.assertTrue(hasaatr(new, "name"))

        """type test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.state_id, str)
        self.assertIsInstance(new.name, str)

        if __name__ == '__main__':
            unittest.main()
