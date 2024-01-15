#!/usr/bin/python3
#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_instance(self):
        """Test Review instance creation"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_review_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    # def test_review_str_representation(self):
    #     """Test Review string representation"""
    #     review = Review()
    #     review.place_id = "place-123"
    #     review.user_id = "user-123"
    #     review.text = "Test Review"
    #     expected_str = '[Review], ({}) {}'.format(review.id, review.__dict__)
    #     self.assertEqual(str(review), expected_str)

    def test_review_to_dict_method(self):
        """Test Review to_dict method"""
        review = Review()
        review.place_id = "place-123"
        review.user_id = "user-123"
        review.text = "Test Review"
        review_dict = review.to_dict()
        expected_dict = {
            'id': review.id,
            'created_at': review.created_at.isoformat(),
            'updated_at': review.updated_at.isoformat(),
            'place_id': "place-123",
            'user_id': "user-123",
            'text': "Test Review",
            '__class__': 'Review'
        }
        self.assertEqual(review_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
