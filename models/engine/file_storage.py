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



# class FileStorage:
    
#     __file_path = "file.json"

#     __objects = {}

#     CLASSES = {
#         'BaseModel': BaseModel,
#         'State': State,
#         'City': City,
#         'Amenity': Amenity,
#         'Place': Place,
#         'Review': Review,
#         'User': User
#     }

#     def __init__(self):
#         self.__file_path = "file.json"
#         self.__objects = {}
    
#     def all(self):
#         """Returns the dictionary __objects."""
#         return self.__objects
    
#     def new(self, obj):
#         """Sets in __objects the obj with key <obj class name>.id."""
#         key = "{}.{}".format(obj.__class__.__name__, obj.id)
#         self.__objects[key] = obj
        

#     def save(self):
#         """Serializes __objects to the JSON file (path: __file_path)."""
#         serialized_objs = {}
#         for key, obj in self.__objects.items():
#             serialized_objs[key] = obj.to_dict()
#         with open(self.__file_path, 'w', encoding='utf-8') as file:
#             json.dump(serialized_objs, file)
    
#     # def reload(self):
#     #     """
#     #     Serializes instances in __objects to JSON and writes them to the JSON file.
#     #     """
#     #     try:
#     #         with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
#     #             obj_dict = json.load(file)
#     #         for key, value in obj_dict.items():
#     #             class_name, obj_id = key.split('.')
#     #             obj_dict[key]['created_at'] = datetime.strptime(value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
#     #             obj_dict[key]['updated_at'] = datetime.strptime(value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
#     #             obj_instance = eval(class_name)(**value)
#     #             FileStorage.__objects[key]= obj_instance
#     #     except FileNotFoundError:
#     #         pass
#     def reload(self):
#         """Deserializes the JSON file to __objects (only if the file exists)."""
#         try:
#             with open(self.__file_path, 'r', encoding='utf-8') as file:
#                 loaded_objs = json.load(file)
#             for key, value in loaded_objs.items():
#                 class_name, obj_id = key.split('.')
#                 obj = FileStorage.CLASSES[class_name](**value)
#                 self.__objects[key] = obj
#         except FileNotFoundError:
#             pass
    
#     def classes(self):
#         """Returns a dictionary of valid classes for serialization."""
#         from models.base_model import BaseModel
#         from models.user import User
#         return {"BaseModel": BaseModel, "User": User}
    
    



class FileStorage:
    """ This is a storage engine for AirBnB clone project
    Class Methods:
        all: Returns the object
        new: updates the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.
    Class Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        class_dict (dict): A dictionary of all the classes.
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

   
    def all(self, cls=None):
        '''Return dictionary of <class>.<id> : object instance'''
        if cls is not None:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects
    
    def delete(self, obj=None):
        '''Deletes obj from __objects if it’s inside'''
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects.pop(key, None)
    

    def new(self, obj):
        '''Set new __objects to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
    def close(self):
        """
            Calls the reload method for deserializing the JSON file to Object
        """
        self.reload()