#!/usr/bin/python3
import unittest
import uuid
from models.base_model import BaseModel
from models.state import State 



class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_create_instance_of_state(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_create(self):
        self.assertIsInstance(self.state, State)

    def test_set_name(self):
        self.state.name = "EGY"
        self.assertEqual(self.state.name, "EGY")

    def test_has_attr(self):
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_for_id(self):
        self.assertIsInstance(uuid.UUID(self.state.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()