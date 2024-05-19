#!/usr/bin/python3
"""
Module for testing FileStorage class.
"""

from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test Suite for the FileStorage class."""

    def test_instances(self):
        """Test instantiation of FileStorage."""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test for the presence of docstrings in FileStorage methods."""
        self.assertIsNotNone(FileStorage.all.__doc__, "all method needs a docstring")
        self.assertIsNotNone(FileStorage.new.__doc__, "new method needs a docstring")
        self.assertIsNotNone(FileStorage.save.__doc__, "save method needs a docstring")
        self.assertIsNotNone(FileStorage.reload.__doc__, "reload method needs a docstring")

    if __name__ == '__main__':
        unittest.main()