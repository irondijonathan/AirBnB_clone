#!/usr/bin/python3
"""To defint the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This represents a user

    Public Class Attributes:
    email: email of user(str)
    password: user password(str)
    first_name: user's first name(str)
    last_name: user's last name(str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
