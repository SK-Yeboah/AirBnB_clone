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


class TestBaseModel(unittest.TestCase):
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

    def test_to_dict_method(self):
        obj_dict = self.my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], str(self.my_model.id))
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], self.my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.my_model.updated_at.isoformat())

    def test_json_representation(self):
        json_repr = self.my_model.to_json()
        self.assertIsInstance(json_repr, str)
        expected_json = '{"id": "' + str(self.my_model.id) + '", "__class__": "BaseModel", "created_at": "' + self.my_model.created_at.isoformat() + '", "updated_at": "' + self.my_model.updated_at.isoformat() + '"}'
        self.assertEqual(json_repr, expected_json)
    
    def test_from_dict_method(self):
        obj_dict = self.my_model.to_dict()
        new_model = BaseModel(**obj_dict)
        self.assertEqual(new_model.id, self.my_model.id)
        self.assertEqual(new_model.created_at, self.my_model.created_at)
        self.assertEqual(new_model.updated_at, self.my_model.updated_at)

    def test_json_serialization(self):
        json_repr = self.my_model.to_json()
        new_model = BaseModel.from_json(json_repr)
        self.assertEqual(new_model.id, self.my_model.id)
        self.assertEqual(new_model.created_at, self.my_model.created_at)
        self.assertEqual(new_model.updated_at, self.my_model.updated_at)

    if __name__ == '__main__':
        unittest.main()
