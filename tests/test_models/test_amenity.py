#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        self.resetStorage()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        a = Amenity()
        for key, value_type in attributes.items():
            self.assertTrue(hasattr(a, key))
            self.assertEqual(type(getattr(a, key, None)), value_type)

if __name__ == "__main__":
    unittest.main()