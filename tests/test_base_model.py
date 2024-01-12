#!/usr/bin/python3
"""
Module test_base_model

This module contains test for base_model
"""

import unittest
import json
import sys
from os import path


project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel:
    """Test for Base Model Class"""
    
    def setUp(self):
        self.my_model =  BaseModel

    def test_init(self):
        """
         Initialization method run before each test.
         Creates an instance of the BaseModel class for testing.
        """
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def text_string_rep(self):
        """
        Tests the string representation of the BaseModel instance.
        Checks if the string representation contains the expected elements.
        """
        string_repr = str(self.my_model)
        self.assertIn("[BaseModel]", string_repr)
        self.assertIn(str(self.my_model.id), string_repr)
        self.assertIn(str(self.my_model.__dict__), string_repr)

    def test_save_method(self):
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_updated_at, self.my_model.updated_at)