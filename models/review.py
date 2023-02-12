#!/usr/bin/python
"""Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """implementation of Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review class initialization"""
        super().__init__(*args, **kwargs)
