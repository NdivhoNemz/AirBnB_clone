#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import unittest
import os
import re
import json
import time
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up the test environment. This is run before each test."""
        self.reset_storage()

    def tearDown(self):
        """Tear down the test environment. This is run after each test."""
        self.reset_storage()

    def reset_storage(self):
        """Reset the FileStorage data to a clean state."""
        FileStorage._FileStorage__objects = {}  # Clear the objects dictionary
        if os.path.isfile(FileStorage._FileStorage__file_path):  # Check if file exists
            os.remove(FileStorage._FileStorage__file_path)  # Remove the storage file

    def test_instantiation(self):
        """Test instantiation of the BaseModel class."""
        b = BaseModel()
        # Check the type and inheritance of the created instance
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_init_no_args(self):
        """Test __init__ with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()  # This should raise a TypeError
        self.assertEqual(str(e.exception), "__init__() missing 1 required positional argument: 'self'")

    def test_init_many_args(self):
        """Test __init__ with many arguments."""
        args = [i for i in range(1000)]  # Create a list of 1000 integers
        BaseModel(*args)  # This should work without raising an exception

    def test_attributes(self):
        """Test attribute values for an instance of BaseModel."""
        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        # Check that the instance has the expected attributes with correct types
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_datetime_created(self):
        """Test if updated_at and created_at are set correctly at creation."""
        date_now = datetime.now()
        b = BaseModel()
        # Check the difference between updated_at and created_at is minimal
        self.assertTrue(abs((b.updated_at - b.created_at).total_seconds()) < 0.01)
        # Check the difference between created_at and current time is minimal
        self.assertTrue(abs((b.created_at - date_now).total_seconds()) < 0.1)

    def test_id(self):
        """Test for unique user IDs."""
        ids = [BaseModel().id for _ in range(1000)]  # Create 1000 instances
        # Check that all generated IDs are unique
        self.assertEqual(len(set(ids)), len(ids))

    def test_save(self):
        """Test the save() method."""
        b = BaseModel()
        time.sleep(0.5)  # Wait to ensure a time difference
        date_now = datetime.now()
        b.save()  # Call the save method
        # Check that updated_at is correctly updated
        self.assertTrue(abs((b.updated_at - date_now).total_seconds()) < 0.01)

    def test_str(self):
        """Test the __str__ method."""
        b = BaseModel()
        # Use regex to check the format of the string representation
        match = re.match(r"^\[(.*)\] \((.*)\) (.*)$", str(b))
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "BaseModel")
        self.assertEqual(match.group(2), b.id)
        s = match.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)  # Normalize datetime string
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_to_dict(self):
        """Test the to_dict() method."""
        b = BaseModel()
        b.name = "Laura"
        b.age = 23
        d = b.to_dict()
        # Check that the dictionary has correct key-value pairs
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)

    def test_to_dict_no_args(self):
        """Test to_dict() with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        self.assertEqual(str(e.exception), "to_dict() missing 1 required positional argument: 'self'")

    def test_to_dict_excess_args(self):
        """Test to_dict() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        self.assertEqual(str(e.exception), "to_dict() takes 1 positional argument but 2 were given")

    def test_instantiation_with_kwargs(self):
        """Test instantiation with **kwargs."""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        # Check that the new instance created from dict matches the original instance
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_instantiation_dict(self):
        """Test instantiation with **kwargs from a custom dict."""
        d = {
            "__class__": "BaseModel",
            "updated_at": datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": str(uuid.uuid4()),
            "var": "foobar",
            "int": 108,
            "float": 3.14
        }
        o = BaseModel(**d)
        # Check that the instance created from dict matches the original dict
        self.assertEqual(o.to_dict(), d)

    def test_save_storage_call(self):
        """Test that storage.save() is called from save()."""
        b = BaseModel()
        b.save()
        key = f"{type(b).__name__}.{b.id}"
        d = {key: b.to_dict()}
        # Check that the file was created and contains correct data
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_no_args(self):
        """Test save() with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        self.assertEqual(str(e.exception), "save() missing 1 required positional argument: 'self'")

    def test_save_excess_args(self):
        """Test save() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        self.assertEqual(str(e.exception), "save() takes 1 positional argument but 2 were given")


if __name__ == '__main__':
    unittest.main()