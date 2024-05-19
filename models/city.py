#!/usr/bin/python3
"""Module for City class."""

from models.base_model import BaseModel

class City(BaseModel):
    """Class representing a City."""
    state_id = ""  # The ID of the state associated with the city
    name = ""      # The name of the city