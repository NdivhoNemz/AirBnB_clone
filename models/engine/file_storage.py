#!/usr/bin/python3
"""Module for FileStorage class."""

import datetime
import json
import os

class FileStorage:
    """Class for serialization and deserialization of base classes."""

    # Private class attributes for file path and object storage
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects.
        
        Returns:
            dict: The dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary.
        
        Args:
            obj (BaseModel): The object to add to the storage.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)  # Create a unique key for the object
        FileStorage.__objects[key] = obj  # Add the object to the dictionary

    def save(self):
        """Serializes the storage dictionary to a JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            # Convert each object to a dictionary before serialization
            obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)  # Write the serialized objects to the file

    def classes(self):
        """Returns a dictionary of valid classes and their references.
        
        Returns:
            dict: A dictionary mapping class names to class references.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        # Dictionary mapping class names to class references
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """Deserializes the JSON file back into the storage dictionary."""
        if not os.path.isfile(FileStorage.__file_path):
            return  # Exit if the file does not exist

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)  # Load the JSON file
            # Recreate the objects from their dictionaries
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict  # Update the storage dictionary with deserialized objects

    def attributes(self):
        """Returns the valid attributes and their types for each class.
        
        Returns:
            dict: A dictionary mapping class names to their valid attributes and types.
        """
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes