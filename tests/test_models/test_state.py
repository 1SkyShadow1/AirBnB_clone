#!/usr/bin/python3
"""
test for State
class
"""
import unittest
from datetime import datetime
from models.state import state


class StateTest(unittest.TestCase):
    """
    State test
    class
    """

    def test_state(self):
        """
        Ensure presence
        of essential
        attributes
        """
        my_instance = State()
        self.assertTrue(hasattr(my_instance, "id"))
        self.assertTrue(hasattr(my_instance, "created_at"))
        self.assertTrue(hasattr(my_instance, "updated_at"))
        self.assertTrue(hasattr(my_instance, "name"))

        """
        Check the
        Attribute types
        """
        self.assertIsInstance(my_instance.id, str)
        self.assertIsInstance(my_instance.created_at, datetime)
        self.assertIsInstance(my_instance.updated_at, datetime)
        self.assertIsInstance(my_instance.name, str)


        if __name__ == '__main__':
            unittest.main()
