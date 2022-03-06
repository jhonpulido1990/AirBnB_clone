#!/usr/bin/python3
"""
Module has:
Imports from our archived base_model
A class inherits BaseModel
And a function init
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class:
    The class name is Review and has a publics atributtes calls placer, user,
    text, this class has a function init with two parameters *args and **kwargs
    """
    place_id = ""
    user_id = ""
    text = ""
