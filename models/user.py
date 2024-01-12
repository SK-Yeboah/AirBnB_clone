#!/usr/bin/python3
import sys
from os import path


# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

from models.base_model import BaseModel

class User(BaseModel):
    """User Class That Inherit From The Base Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    