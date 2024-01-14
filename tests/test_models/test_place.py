#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Class to test place class
    """
    def setUp(self):
        """
        This method is called before each
        test method in the test class
        """
        self.place = Place()

    def test_create_instance_of_place(self):
        """
        Tests create instance of place
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_create(self):
        """
        test for create
        """
        self.assertIsInstance(self.place, Place)

    def test_set_name(self):
        """
        Test for set name
        """
        self.place.name = "room"
        self.assertEqual(self.place.name, "room")

    def test_has_attr(self):
        """
        Test for attrbuite
        """
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertTrue(hasattr(self.place, "latitude"))

    def test_for_id(self):
        """
        Test for id
        """
        self.assertIsInstance(uuid.UUID(self.place.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
