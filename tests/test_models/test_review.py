#!/usr/bin/python3
import unittest
import uuid
from models.base_model import BaseModel
from models.review import Review 



class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_create_instance_of_review(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_create(self):
        self.assertIsInstance(self.review, Review)

    def test_set_name(self):
        self.review.text = "Very good"
        self.assertEqual(self.review.text, "Very good")

    def test_has_attr(self):
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))

    def test_for_id(self):
        self.assertIsInstance(uuid.UUID(self.review.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()