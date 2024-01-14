#!/usr/bin/python3
"""
Unit tests for the FileStorage class in the models.engine.file_storage module.

Methods:
- test_FileStorage_init: Test the initialization of the FileStorage class.
- test_all: Test the all method of the FileStorage class.
- test_new: Test the new method of the FileStorage class.
- test_save: Test the save method of the FileStorage class.
- test_reload: Test the reload method of the FileStorage class.
- etc...
"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test file storage class
    """
    def test_FileStorage_init(self):
        """
        Test file storage for init
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_all(self):
        """
        Test all method that returns the dictionary __objects
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_file_path_type(self):
        """
        Test file path for type
        """
        self.assertEqual(str, type(FileStorage()._FileStorage__file_path))

    def test_storage_type(self):
        """
        Test storage file for type
        """
        self.assertEqual(type(models.storage), FileStorage)

    def test_new(self):
        """
        Test in __objects the obj with key
        <obj class name>.id
        """
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())

    def test_successfully_adds_new_object(self):
        """
        Test successfully add new obj
        """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(obj, models.storage.all().values())

    def test_can_add_multiple_objects(self):
        """
        Test for all adds mulltiply obj
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        self.assertIn(obj1, models.storage.all().values())
        self.assertIn(obj2, models.storage.all().values())

    def test_save(self):
        """
        Test save funtion
        """
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + base.id, save_text)
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """
        Test reload function
        """
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage()._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
