#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_init(self):
        """Test Amenity initialization"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)  # Assuming Amenity is supposed to inherit from BaseModel

    def test_str_representation(self):
        """Test Amenity string representation"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        expected_str = '[Amenity], ({})'.format(amenity.id)
        self.assertEqual(str(amenity)[:len(expected_str)], expected_str)


if __name__ == '__main__':
    unittest.main()
