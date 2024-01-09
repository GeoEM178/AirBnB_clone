#!/usr/bin/python3
import json
import os
"""_summary_

Returns:
    _type_: _description_
"""
class FileStorage:
    """_summary_

    Returns:
        _type_: _description_
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return FileStorage.__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """_summary_
        """
        all_objects = FileStorage.__objects
        objects_dictionary = {}

        for object in all_objects.keys():
            objects_dictionary[object] = all_objects[object].to_dict()

        with open(FileStorage.__file_path, "a") as f:
            json.dump(objects_dictionary, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    from_json_dict = json.loads(f)
                    for key, value in from_json_dict.items():
                        class_name, obj_id = key.split('.')
                        temp = eval(class_name)
                        obj = temp(**value)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass