#!/usr/bin/python3
"""Definition of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represents a review

    Public Class Attributes:
    place_id: it will be the Place.id (str)
    user_id: it will be the User.id (str)
    text: empty string (str)
    """
    place_id = ""
    user_id = ""
    text = ""
