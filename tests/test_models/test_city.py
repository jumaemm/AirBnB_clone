#!/usr/bin/python3
"""Test suite for the City class of the models.city module"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Create a Case instance"""
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_city_is_a_subclass_of_basemodel(self):
        """Test that City is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.city), BaseModel))
