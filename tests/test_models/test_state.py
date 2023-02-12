#!/usr/bin/python3
"""Test suite for the State class of the models.state module"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Create a state instance"""
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        """Test that state is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        """Test that state has the name attribute"""
        self.assertTrue(hasattr(self.state, "name"))
