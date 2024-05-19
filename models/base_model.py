#!/usr/bin/python3
"""Module for BaseModel class.
Contains the BaseModel class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for the AirBnB clone console project.
    
    This class provides a base model for other classes in the project.
    It includes common attributes and methods such as id, created_at,
    updated_at, save, and to_dict.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance.

        This constructor can initialize the instance with keyword arguments,
        typically used for creating an instance from a dictionary (e.g., deserialization).

        Args:
            - *args: list of arguments (not used)
            - **kwargs: dictionary of key-value arguments to initialize instance attributes
        """
        if kwargs:
            # Initialize from keyword arguments
            for key, value in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    # Convert string dates to datetime objects
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            # Default initialization for new instances
            self.id = str(uuid.uuid4())  # Generate a unique id
            self.created_at = datetime.now()  # Set the creation time to now
            self.updated_at = datetime.now()  # Set the last update time to now
            storage.new(self)  # Register the new instance in storage

    def __str__(self):
        """Return a string representation of the instance.

        This provides a human-readable representation of the instance,
        including its class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime and save.

        This method updates the updated_at attribute to the current datetime
        and then saves the instance to storage.
        """
        self.updated_at = datetime.now()  # Update the last update time to now
        storage.save()  # Save the updated instance in storage

    def to_dict(self):
        """Return a dictionary representation of the instance.

        This method creates a dictionary representation of the instance,
        including class name, and ensuring datetime attributes are converted to strings.

        Returns:
            dict: A dictionary containing all instance attributes.
        """
        my_dict = self.__dict__.copy()  # Create a copy of the instance's dictionary
        my_dict["__class__"] = self.__class__.__name__  # Add the class name
        my_dict["created_at"] = self.created_at.isoformat()  # Convert created_at to string
        my_dict["updated_at"] = self.updated_at.isoformat()  # Convert updated_at to string
        return my_dict