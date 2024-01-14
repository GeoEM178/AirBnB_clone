#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Class to test amenity class
    """
    def setUp(self):
        """
        This method is called before
        each test method in the test class
        """
        self.amenity = Amenity()

    def test_create_instance_of_amenity(self):
        """
        Test create instance of amenity
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_create(self):
        """
        Tests create function
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_set_name(self):
        """
        Test set name
        """
        self.amenity.name = "Mostafa"
        self.assertEqual(self.amenity.name, "Mostafa")

    def test_has_attr(self):
        """
        Tests has attrbuite
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_for_id(self):
        """
        Tests for id
        """
        self.assertIsInstance(uuid.UUID(self.amenity.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
