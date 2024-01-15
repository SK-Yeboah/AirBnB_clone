#!/usr/bin/python3 

import sys
import os
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

import unittest
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Backup the original file path and create a temporary file path
        self.original_file_path = storage._FileStorage__file_path
        storage._FileStorage__file_path = "test_file.json"

    def tearDown(self):
        # Restore the original file path and remove the temporary file
        storage._FileStorage__file_path = self.original_file_path
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_all_new_save_reload(self):
        # Ensure 'all', 'new', 'save', and 'reload' work together
        storage.reload()
        all_objs_before = storage.all()

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        storage.reload()
        all_objs_after = storage.all()

        # Check that the new model is in the dictionary
        self.assertIn(my_model.id, all_objs_after)

        # Check that the contents of the new model are the same
        self.assertEqual(my_model.to_dict(), all_objs_after[my_model.id].to_dict())

        # Check that all other objects are the same
        for key, value in all_objs_before.items():
            if key != my_model.id:
                self.assertEqual(value.to_dict(), all_objs_after[key].to_dict())



    def test_file_content_after_save(self):
        # Ensure the content of the file matches the serialized objects
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        with open("test_file.json", 'r') as file:
            file_content = file.read()
            self.assertIn(my_model.id, file_content)

    def test_reload_nonexistent_file(self):
        # Ensure reload doesn't raise an exception if the file doesn't exist
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

        storage.reload()

        # If no exception is raised, the test is successful

    def test_reload_with_existing_file(self):
        # Ensure reload works with an existing file
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        storage.reload()

        reloaded_objs = storage.all()

        self.assertIn(my_model.id, reloaded_objs)
        self.assertEqual(my_model.to_dict(), reloaded_objs[my_model.id].to_dict())

    def test_reload_with_multiple_objects(self):
        # Ensure reload works with multiple objects in the file
        model_1 = BaseModel()
        model_1.name = "Model_1"
        model_1.save()

        user = User()
        user.email = "test@example.com"
        user.save()

        storage.reload()

        reloaded_objs = storage.all()

        self.assertIn(model_1.id, reloaded_objs)
        self.assertIn(user.id, reloaded_objs)

if __name__ == '__main__':
    unittest.main()
