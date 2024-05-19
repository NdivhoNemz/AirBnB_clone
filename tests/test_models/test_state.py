#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
import os
from models.state import State
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

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
        """Tests instantiation of State class."""
        state_instance = State()
        self.assertEqual(str(type(state_instance)), "<class 'models.state.State'>")
        self.assertIsInstance(state_instance, State)
        self.assertTrue(issubclass(type(state_instance), BaseModel))

    def test_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        state_instance = State()
        for attribute_name, attribute_type in attributes.items():
            self.assertTrue(hasattr(state_instance, attribute_name))
            self.assertEqual(type(getattr(state_instance, attribute_name, None)), attribute_type)


if __name__ == "__main__":
    unittest.main()