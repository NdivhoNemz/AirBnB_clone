#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

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
        """Tests instantiation of Review class."""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        review = Review()
        for attr, attr_type in attributes.items():
            self.assertTrue(hasattr(review, attr))
            self.assertEqual(type(getattr(review, attr, None)), attr_type)

if __name__ == "__main__":
    unittest.main()