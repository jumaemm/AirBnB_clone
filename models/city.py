#!/usr/bin/env python3
"""This inherits from BaseModel class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This represents the city the apartment is located in

    Attributes:
        state_id (str): id of the state
        name (str): name of the city
    """
    state_id = ""
    name = ""
