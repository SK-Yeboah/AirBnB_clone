#!/usr/bin/python3
"""Module base_model

This Module contains a definition for City Class
"""
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)
from models.base_model import BaseModel

class City(BaseModel):
    """A class that represents a city

    Attributes:
        name (str): name of the city
        state_id (str): the state id
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance"""
        super().__init__(*args, **kwargs)
