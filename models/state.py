#!/usr/bin/python3
"""Module has: Imports from our archived base_model
A class inherits BaseModel And a function init"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class: The class name is State and has a public atributte call "name"
    this class has a function init with two parameters *args and **kwargs

    Args:
        name (Str): The name of the state. """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Funciont: This function receives two parameters *args(arguments)
        and **kwargs(number of arguments)"""
        super().__init__(*args, **kwargs)
