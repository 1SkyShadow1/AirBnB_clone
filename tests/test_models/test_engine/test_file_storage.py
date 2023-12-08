#!/usr/bin/python3
"""
unit test
for bases
"""
import unittest
import json
import models.base_model import BaseModel
import models
import os

class FileStorageTest(unittest.TestCase):
    """
    unit test for File
    storage
    """
    def test_FileStorage_init(self):
        storage_objs = models.storage._FileStorage__objects
        flPath = models.storage._FileStorage__file_path
        """
        test to check
        class attribute
        """
        self.assertEqual(flPath, "file.json")
        self.assertIsInstance(flPath, str)
        self.assertIsInstance(storage_objs, dict)
        my_instance = BaseModel()
        """
        check if methods
        are available
        """
        self.assertTrue(hasattr(my_instance, "__init__"))
        self.assertTrue(hasattr(my_instance, "__str__"))
        self.assertTrue(hasattr(my_instance, "to_dict"))
        self.assertTrue(hasattr(my_instance, "save"))

        """
        Test all
        methods
        """
        self.assertNotEqual(models.storage.all(), {})
        self.assertIsInstance(model.storage.all(), dict)

        """
        Test if has
        id
        """
        self.assertTrue(hasattr(my_instance, "id"))
        self.assertIsInstance(my_instance.id, str)

        """
        """
        nameOfKey = "BaseModel."+my_instance.id

        """
        check if
        object exists by
        name of the key
        """
        self.assertIn(nameOfKey, models.storage.all())
        """
        check if the object in
        storage has correct id
        """
        self.assertTrue(models.storage.all()[nameOfKey] is my_instance)
        self.assertIsInstance(models.storage.all()[nameOfKey], BaseModel)
        self.asserEqual(models.storage.all()[nameOfKey], my_instance)
        """
        Reload a file
        """
        models.storage.all().clear()
        models.storage.reload()
        with open(flPath, 'r') as fl:
            data = json.load(fl)
        self.assertEqual(data[nameOfKey],
                         models.storage.all()[nameOfKey].to_dict())

        """
        Save a file
        """
        models.storage.save()
        with open(flPath, 'r') as fl:
            data = json.load(fl)
         """
         Object in json is
         correct
         """
         self.assertEqual(data[nameOfKey], my_instance.to_dict())
         """
         Does object
         exist by name of the key
         """
         self.assetrIn(nameOfKey, data)

         """
         file
         """
         if os.path.exists(flPath):
             os.remove(flPath)
        self.assertFalse(os.path.exists(flPath))
        models.storage.reload()


if __name__ = '__main__':
    unittest.main()
