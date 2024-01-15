#!/usr/bin/python3
import unittest
import sys
from os import path
from datetime import datetime
import json

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    def test_state_attributes(self):
        """Test the attributes of the State class."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_inheritance(self):
        """Test if the State class inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_initialization(self):
        """Test the initialization of the State instance."""
        state_data = {'name': 'test_state'}
        state = State(**state_data)

        for key, value in state_data.items():
            self.assertEqual(getattr(state, key), value)

    def test_state_str_representation(self):
        """Test the __str__ method of the State class."""
        state_data = {'name': 'test_state'}
        state = State(**state_data)
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)

        self.assertEqual(str(state), expected_str)

    def test_state_to_dict(self):
        """Test the to_dict method of the State class."""
        state_data = {'name': 'test_state'}
        state = State(**state_data)
        state_dict = state.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at'] + list(state_data.keys())
        for key in expected_keys:
            self.assertIn(key, state_dict)

        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], state.updated_at.isoformat())

    def test_state_json_serialization(self):
        """Test JSON serialization of the State instance."""
        state_data = {'name': 'test_state'}
        state = State(**state_data)

        json_str = json.dumps(state.to_dict())
        state_dict = json.loads(json_str)

        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], state.updated_at.isoformat())
        for key, value in state_data.items():
            self.assertEqual(state_dict[key], value)

    def test_state_json_deserialization(self):
        """Test JSON deserialization of the State instance."""
        state_data = {'name': 'test_state'}
        state = State(**state_data)

        state_json = json.dumps(state.to_dict())
        new_state = State(**json.loads(state_json))

        self.assertEqual(new_state.id, state.id)
        self.assertEqual(new_state.created_at, state.created_at)
        self.assertEqual(new_state.updated_at, state.updated_at)
        for key, value in state_data.items():
            self.assertEqual(getattr(new_state, key), value)

if __name__ == '__main__':
    unittest.main()
