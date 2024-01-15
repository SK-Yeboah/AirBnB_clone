#!/usr/bin/python3
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()