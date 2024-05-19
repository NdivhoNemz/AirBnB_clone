#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class representing an Amenity.

    Inherits from BaseModel.

    Attributes:
        name (str): The name of the amenity. Default is an empty string.
    """
    name = ""