#!/usr/bin/python3
"""Unittests for models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_attrs_are_class_attrs(self):
        """Tests for the presence of the public class attrs"""
        u = User()
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_types_attrs(self):
        """Tests that the attributes are of the expected types"""
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        """Tests that User is a subclass of the BaseModel class"""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
