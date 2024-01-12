#!/usr/bin/python3

import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)
from models.base_model import BaseModel

class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)
