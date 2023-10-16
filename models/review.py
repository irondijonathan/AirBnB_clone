#!/usr/bin/python3
"""This is the Definition of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the representation of a review

    Public Class Attributes:
    place_id: it will be the Place.id (str)
    user_id: it will be the User.id (str)
    text: empty string (str)
    """
    place_id = ""
    user_id = ""
    text = ""
