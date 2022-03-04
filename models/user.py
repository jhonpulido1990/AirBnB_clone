#!/usr/bin/python3

from models.base_model import BaseModel
"""Import our BaseModel from our archived base_model"""


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
