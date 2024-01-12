#!/usr/bin/python3
"""
File storage module
This module is responsible for serialization and deserialization of various classes to and from json file
"""

import json
from datetime import datetime
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class FileStorage:
    
    # __file_path = "file.json"

    # __objects = {}

    CLASSES = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        'User': User
    }

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)
    
    # def reload(self):
    #     """
    #     Serializes instances in __objects to JSON and writes them to the JSON file.
    #     """
    #     try:
    #         with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
    #             obj_dict = json.load(file)
    #         for key, value in obj_dict.items():
    #             class_name, obj_id = key.split('.')
    #             obj_dict[key]['created_at'] = datetime.strptime(value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
    #             obj_dict[key]['updated_at'] = datetime.strptime(value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
    #             obj_instance = eval(class_name)(**value)
    #             FileStorage.__objects[key]= obj_instance
    #     except FileNotFoundError:
    #         pass
    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objs = json.load(file)
            for key, value in loaded_objs.items():
                class_name, obj_id = key.split('.')
                obj = FileStorage.CLASSES[class_name](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
    
    def classes(self):
        """Returns a dictionary of valid classes for serialization."""
        from models.base_model import BaseModel
        from models.user import User
        return {"BaseModel": BaseModel, "User": User}
    
    