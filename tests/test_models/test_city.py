#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_instance(self):
        """Test City instance creation"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    # def test_city_str_representation(self):
    #     """Test City string representation"""
    #     city = City()
    #     city.state_id = "state-123"
    #     city.name = "Test City"
    #     expected_str = '[City], ({}) {}'.format(city.id, city.__dict__)
    #     self.assertEqual(str(city), expected_str)



    def test_city_to_dict_method(self):
        """Test City to_dict method"""
        city = City()
        city.state_id = "state-123"
        city.name = "Test City"
        city_dict = city.to_dict()
        expected_dict = {
            'id': city.id,
            'created_at': city.created_at.isoformat(),
            'updated_at': city.updated_at.isoformat(),
            'state_id': "state-123",
            'name': "Test City",
            '__class__': 'City'
        }
        self.assertEqual(city_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
