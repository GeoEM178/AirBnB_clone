#!/usr/bin/python3
import unittest
import uuid
from models.base_model import BaseModel
from models.user import User 


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_create_instance_of_user(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_create(self):
        self.assertIsInstance(self.user, User)

    def test_set_name(self):
        self.user.name = "EGY"
        self.assertEqual(self.user.name, "EGY")

    def test_has_attr(self):
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_for_id(self):
        self.assertIsInstance(uuid.UUID(self.user.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()