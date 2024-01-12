#!/usr/bin/python3
"""Place Module"""
import sys
from os import path

# Add the project directory to the Python path
project_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(project_path)
from models.base_model import BaseModel

class Place(BaseModel):
    """Place Class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize Place Instance"""
        super().__init__(*args, **kwargs)
