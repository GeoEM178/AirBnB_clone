#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Class to test city class
    """
    def setUp(self):
        """
        SetUp finction
        """
        self.city = City()

    def test_create_instance_of_city(self):
        """
        Tests create instance of city
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_create(self):
        """
        tests create function
        """
        self.assertIsInstance(self.city, City)

    def test_set_name(self):
        """
        Tests set name
        """
        self.city.name = "Mokattam"
        self.assertEqual(self.city.name, "Mokattam")

    def test_has_attr(self):
        """
        Tests has attrbute
        """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_for_id(self):
        """
        Test for id
        """
        self.assertIsInstance(uuid.UUID(self.city.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
