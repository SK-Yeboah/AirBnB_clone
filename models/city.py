#!/usr/bin/python3
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)
from models.base_model import BaseModel

class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance"""
        super().__init__(*args, **kwargs)
