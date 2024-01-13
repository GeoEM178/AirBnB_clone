#!/usr/bin/python3
import unittest
import uuid
from models.base_model import BaseModel
from models.amenity import Amenity 



class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_create_instance_of_amenity(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_create(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_set_name(self):
        self.amenity.name = "Mostafa"
        self.assertEqual(self.amenity.name, "Mostafa")

    def test_has_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_for_id(self):
        self.assertIsInstance(uuid.UUID(self.amenity.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()