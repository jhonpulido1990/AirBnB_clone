#!/usr/bin/python3
"""
Module has:
Imports from our archived base_model
A class inherits BaseModel
And a function init
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class:
    The class name is Place and has a publics atributtes calls: city, user,
    name, description, number rooms, number bathrooms and others.
    this class has a function init with two parameters *args and **kwargs
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
