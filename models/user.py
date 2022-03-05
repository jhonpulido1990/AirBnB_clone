#!/usr/bin/python3
"""Module has imports from our archived base_model"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Represents the User class with there arguments:"""

        super().__init__(*args, **kwargs)
