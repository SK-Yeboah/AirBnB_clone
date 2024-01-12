#!/usr/bin/python3
"""Place Module"""
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)
from models.base_model import BaseModel

class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Place Instance"""
        super().__init__(*args, **kwargs)
