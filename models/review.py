#!/usr/bin/python3
"""Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review."""
    place_id = ""  # The ID of the place associated with the review
    user_id = ""   # The ID of the user who created the review
    text = ""      # The text content of the review