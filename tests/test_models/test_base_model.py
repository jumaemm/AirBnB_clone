#!/usr/bin/env python3
"""Module containing tests for the BaseModel class"""

import unittest
import os
from time import sleep
from datetime import datetime
from uuid import uuid4
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_init_id(self):
        """Checks for instance initialization"""
        test_case = BaseModel()
        self.assertTrue(hasattr(test_case, "id"))

    def test_str_rep(self):
        """Check for string representation"""
        test_case = BaseModel()
        self.assertEqual(str(test_case),
                         "[BaseModel] ({}) {}".format(test_case.id, test_case.__dict__))

    def test_unique_uuids(self):
        """Check if uuids are unique"""
        test_case = BaseModel()
        test_case2 = BaseModel()
        self.assertNotEqual(test_case.id, test_case2.id)

    def test_unique_created_at(self):
        """Check if created dates are unique for different instances"""
        test_case = BaseModel()
        sleep(0.04)
        test_case2 = BaseModel()
        sleep(0.04)

    def test_no_args_passed(self):
        """Check that no args are passed"""
        test_case = BaseModel(None)
        self.assertNotIn(None, test_case.__dict__.values())

    def test_kwargs_passed(self):
        """Test that kwargs are passed to create an instance"""
        test_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                     "updated_at": datetime.utcnow().isoformat()}
        test_case = BaseModel(**test_dict)
        self.assertEqual(test_case.id, test_dict["id"])
        self.assertEqual(test_case.created_at,
                         datetime.strptime(test_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(test_case.updated_at,
                         datetime.strptime(test_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_created_at_is_datetime_object(self):
        """Test that created at is a datetime object"""
        test_case = BaseModel()
        self.assertTrue(type(test_case.updated_at) is datetime)

    def test_save_function_updates_date(self):
        """Test that save function updates updated_at attribute"""
        test_case = BaseModel()
        sleep(0.5)
        test_case.save()
        self.assertNotEqual(test_case.created_at, test_case.updated_at)

    def test_to_dict_creates_dict(self):
        """Test that too_dict object creates a dict object"""
        test_case = BaseModel()
        self.assertTrue(type(test_case.to_dict()) is dict)

    def test_save_update_file(self):
        """Tests save functionality"""
        test_case = BaseModel()
        test_case.save()
        test_id = "BaseModel.{}".format(test_case.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(test_id, f.read())

    def test_that_to_dict_contains_correct_keys(self):
        """Checks whether to_dict() returns the correct attributes"""
        test_dict = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, test_dict)

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """Checks that created_at is modified to an ISOformat string"""
        test_case = BaseModel()
        self.assertEqual(test_case.to_dict()["created_at"],
                         test_case.created_at.isoformat())

    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """Checks that updated_at is modified to an ISOformat string"""
        test_case = BaseModel()
        self.assertEqual(test_case.to_dict()["updated_at"],
                         test_case.updated_at.isoformat())
