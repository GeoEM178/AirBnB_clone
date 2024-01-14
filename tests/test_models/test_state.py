#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for base class
    """
    def setUp(self):
        """
        This method is called before each
        test method in the test class
        """
        self.state = State()

    def test_create_instance_of_state(self):
        """
        Test create instance of state
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_create(self):
        """
        Test of create function
        """
        self.assertIsInstance(self.state, State)

    def test_set_name(self):
        """
        Test fo set name
        """
        self.state.name = "EGY"
        self.assertEqual(self.state.name, "EGY")

    def test_has_attr(self):
        """
        Test for attrbuite
        """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_for_id(self):
        """
        Test for id
        """
        self.assertIsInstance(uuid.UUID(self.state.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
