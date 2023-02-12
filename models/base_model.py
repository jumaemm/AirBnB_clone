#!/usr/bin/env python3
"""This module is the base module for all other subclasses"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Class representing the base of all other models
    """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance
        Arguments:
            *args: arguments
            **kwargs: keyword arguments array
        """

        if (kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key not in ("created_at", "updated_at"):
                        setattr(self, key, value)
                    else:
                        setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save the new instance to a file"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Create a JSON representation of a BaseModel instance
        """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key in new_dict.keys():
            if key in ("created_at", "updated_at"):
                value = new_dict[key].isoformat()
                new_dict[key] = value
        return new_dict
