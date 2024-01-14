#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Class to test user class
    """
    def setUp(self):
        """
        This method is called before each
        test method in the test class
        """
        self.user = User()

    def test_create_instance_of_user(self):
        """
        Test create function of user
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_create(self):
        """
        Test create
        """
        self.assertIsInstance(self.user, User)

    def test_set_name(self):
        """
        Test set funtion for set name
        """
        self.user.name = "EGY"
        self.assertEqual(self.user.name, "EGY")

    def test_has_attr(self):
        """
        Test for attrbuite
        """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_for_id(self):
        """
        Test for id
        """
        self.assertIsInstance(uuid.UUID(self.user.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
