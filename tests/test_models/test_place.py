#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

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
        """Tests instantiation of Place class."""

        b = Place()
        # Verify the type of the instance
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        # Verify if the instance is an instance of Place class
        self.assertIsInstance(b, Place)
        # Verify if the instance is a subclass of BaseModel
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Place class."""
        # Get the attributes dictionary for the Place class
        attributes = storage.attributes()["Place"]
        # Create a Place instance
        o = Place()
        # Iterate through each attribute and verify its presence and type
        for k, v in attributes.items():
            # Verify if the attribute exists
            self.assertTrue(hasattr(o, k))
            # Verify the type of the attribute
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()