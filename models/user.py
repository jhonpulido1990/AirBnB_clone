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
    Attributes:
        email     The maximum speed that such a bird can attain.
        password  The locale where these birds congregate to reproduce.
        first_name     The maximum speed that such a bird can attain.
        last_name  The locale where these birds congregate to reproduce.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Represents the User class with there arguments:"""
        super().__init__(*args, **kwargs)
