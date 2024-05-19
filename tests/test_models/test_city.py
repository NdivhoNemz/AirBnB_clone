#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.base_model import BaseModel
from models.city import City  # Import the City class to be tested
from models.engine.file_storage import FileStorage  # Import FileStorage for storage handling
import os
from models import storage  # Import storage for accessing attributes

class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of City class."""
        b = City()
        # Check if the instance is of the correct class and inherits from BaseModel
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """Tests the attributes of City class."""
        # Get the attributes for City from storage
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            # Check if each attribute exists and has the correct type
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()