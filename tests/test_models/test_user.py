#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods.

        This method is called before each test. It's used to set up any state
        that's shared among the tests.
        """
        self.resetStorage()

    def tearDown(self):
        """Tears down test methods.

        This method is called after each test. It's used to clean up any state
        that was set up in the setUp method.
        """
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data.

        This method clears the storage by resetting the __objects dictionary
        and removing the JSON file if it exists.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class.

        This test checks if a User instance is correctly created and if it
        is an instance of the User class and a subclass of BaseModel.
        """
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class.

        This test checks if the User instance has the correct attributes
        with the expected types.
        """
        attributes = storage.attributes()["User"]
        user = User()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(user, attr_name))
            self.assertEqual(type(getattr(user, attr_name, None)), attr_type)

if __name__ == "__main__":
    unittest.main()