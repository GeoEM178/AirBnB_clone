#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Class to test Review class
    """
    def setUp(self):
        """
        This method is called before
        each test method in the test class
        """
        self.review = Review()

    def test_create_instance_of_review(self):
        """
        Test to create instance of review
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_create(self):
        """
        Test for create
        """
        self.assertIsInstance(self.review, Review)

    def test_set_name(self):
        """
        Test for set name
        """
        self.review.text = "Very good"
        self.assertEqual(self.review.text, "Very good")

    def test_has_attr(self):
        """
        Test for attrbuite
        """
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))

    def test_for_id(self):
        """
        Test for id
        """
        self.assertIsInstance(uuid.UUID(self.review.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
