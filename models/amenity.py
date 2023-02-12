#!/usr/bin/python
"""Define class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization Amenity"""
        super().__init__(*args, **kwargs)
