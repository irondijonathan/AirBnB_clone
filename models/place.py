#!/usr/bin/python3
"""Definition of the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This represents a Place

    Public Class Attributes:
    city_id: Id of the city - City.id (str)
    user_id: ID of the user - User.id (str)
    name: name of place(str)
    description: description of the place (str)
    number_rooms: number of rooms (int)
    number_bathrooms: number of bathrooms (int)
    max_guest: max number of guests (int)
    price_by_night: price per night (int)
    latitude: the latitude (float)
    longitude: the longitude (float)
    amenity_ids: list of amenities available (List[str])
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
