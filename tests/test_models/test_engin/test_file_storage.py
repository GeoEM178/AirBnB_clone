"""_summary_
"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_FileStorage_init(self):
        self.assertEqual(type(FileStorage()), FileStorage)
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
    def test_file_path_type(self):
        self.assertEqual(str, type(FileStorage()._FileStorage__file_path))
    def test_storage_type(self):
        self.assertEqual(type(models.storage), FileStorage)
    def test_new(self):
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())
    def test_successfully_adds_new_object(self):
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(obj, models.storage.all().values())
    def test_can_add_multiple_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        self.assertIn(obj1, models.storage.all().values())
        self.assertIn(obj2, models.storage.all().values())
    def test_save(self):
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
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage()._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)
