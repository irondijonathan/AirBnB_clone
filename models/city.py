#!/usr/bin/python3
"""Definition of the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This represents a City

    Public Class Attributes:
    state_id: Id of the state - State.id (str)
    name: name of city(str)
    """
    state_id = ""
    name = ""
