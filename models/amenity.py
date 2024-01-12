#!/usr/bin/python3
"""Amenity Module"""

import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialize The Amenity Instance"""
        super().__init__(*args, **kwargs)
