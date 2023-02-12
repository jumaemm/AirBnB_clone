#!/usr/bin/env python3
"""This inherits from the BaseModel class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents the State/ Location of the apartment

    Attributes:
        name (str): name of the state
    """
    name = ""
