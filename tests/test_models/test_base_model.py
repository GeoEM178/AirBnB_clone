#!/usr/bin/python3
"""
Unit testing for the base_model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Class to test base class
    """

    def test_initialization(self):
        """
        Test if a BaseModel instance is initialized correctly
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test the save method if it updates the updated_at correctly
        """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method if it returns a dictionary correctly
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        created_at_iso = my_model.created_at.isoformat()
        updated_at_iso = my_model.updated_at.isoformat()

        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], created_at_iso)
        self.assertEqual(my_model_dict["updated_at"], updated_at_iso)

    def test_str(self):
        """
        Test the __str__ method if it returns a string correctly
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

    def test_kwargs(self):
        """
        Test the initialization with kwargs
        """
        format_date = "2019-07-01T00:00:00.000000"
        iso_format = datetime.fromisoformat(format_date)
        my_model = BaseModel(created_at=format_date, updated_at=format_date)
        self.assertEqual(my_model.created_at, iso_format)
        self.assertEqual(my_model.updated_at, iso_format)
        self.assertNotEqual(my_model.created_at, datetime.utcnow())
        self.assertNotEqual(my_model.updated_at, datetime.utcnow())


if __name__ == "__main__":
    unittest.main()
