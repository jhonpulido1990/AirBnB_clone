#!/usr/bin/python3
"""
Module has:
Imports from our archived base_model
A class inherits BaseModel
And a function init
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class:
    The class name is User and has a publics atributtes calls email, password,
    first name and last name,this class has a function init with two
    parameters *args and **kwargs
    Args:
        email (str): The email of the user.
        password (str): The password of the user.
        firstname (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Represents the User class with there arguments:"""
        super().__init__(*args, **kwargs)
