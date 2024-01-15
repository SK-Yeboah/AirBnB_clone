#!/usr/bin/python3
"""
Module test_base_model

This module contains test for base_model
"""
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel
from models import storage
import models

class TestBaseModel(unittest.TestCase):

    def test_base_model_attributes(self):
        """Test the attributes of the BaseModel class."""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_base_model_inheritance(self):
        """Test if the BaseModel class inherits from object."""
        base_model = BaseModel()
        self.assertIsInstance(base_model, object)

    def test_base_model_initialization(self):
        """Test the initialization of the BaseModel instance."""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_base_model_str_representation(self):
        """Test the __str__ method of the BaseModel class."""
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)

        self.assertEqual(str(base_model), expected_str)

    def test_base_model_save_method(self):
        """Test the save method of the BaseModel class."""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()

        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_base_model_to_dict_method(self):
        """Test the to_dict method of the BaseModel class."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, base_model_dict)

        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    # def test_base_model_save_to_dict_consistency(self):
    #     """Test the consistency between save and to_dict methods."""
    #     base_model = BaseModel()
    #     base_model_dict = base_model.to_dict()
    #     initial_updated_at = base_model.updated_at
    #     storage.save()

    #     self.assertNotEqual(initial_updated_at, base_model.updated_at)
    #     self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())

   

if __name__ == '__main__':
    unittest.main()
