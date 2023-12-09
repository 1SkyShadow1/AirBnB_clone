#!/usr/bin/python3
"""
unit test
for Review
class
"""
import unittest
from datetime import datetime
from models.review import Review


class ReviewTests(unittest.TestCase):
    """
    Test for Review
    class
    """

    def test_review(self):
        """
        Ensure
        presence of
        essential attributes
        """
        my_instance = Review()

        self.assertTrue(hasattr(my_instance, "id"))
        self.assertTrue(hasattr(my_instance, "created_at"))
        self.assertTrue(hasattr(my_instance, "updated_at"))
        self.assertTrue(hasattr(my_instance, "place_id"))
        self.assertTrue(hasattr(my_instance, "user_id"))
        self.assertTrue(hasattr(my_instance, "text"))

        """
        Check the type
        of attribute
        """
        self.assertIsInstance(my_instance.id, str)
        self.assertIsInstance(my_instance.created_at, datetime)
        self.assertIsInstance(my_instance.updated_at, datetime)
        self.assertIsInstance(my_instance.place_id, str)
        self.assertIsInstance(my_instance.user_id, str)
        self.assertIsInstance(my_instance.text, str)

    if __name__ == '__main__':
        unittest.main()
