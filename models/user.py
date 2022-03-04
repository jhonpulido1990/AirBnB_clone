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
    parameters *args and **kwargs"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Funciont:
        This function receives two parameters *args(arguments)
        and **kwargs(number of arguments)"""
        super().__init__(*args, **kwargs)
