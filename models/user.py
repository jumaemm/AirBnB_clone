#!/usr/bin/env python3
"""This inherits from the BaseModel class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel class

    Attributes:
        email (str): email of the user
        password (str): user password
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
