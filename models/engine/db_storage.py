#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""

import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objs = json.load(file)
                from models.base_model import BaseModel
                for obj_id, obj in objs.items():
                    cls_name = obj['__class__']
                    cls = eval(cls_name)
                    self.new(cls(**obj))
        except FileNotFoundError:
            pass

    def close(self):
        """Reloads JSON file to objects"""
        self.reload()
