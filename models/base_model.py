#!/usr/bin/python3
"""
Module: base_model.py
This is the "base model" module.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel is a base for all the classes - will be inherited

    Attributes:
      id(str): the unique id of the instance(user)
      created_at: when the instance created
      updated_at: when the instance updated

    Methods:
      __str__: return class name, instance id, and the dictionary
      save(self): updates instance updated_at
      to_dict(self): returns the dictionary keys and values of the object

    """
    def __init__(self, *args, **kwargs):
        """Instance Constructor initialization

        Args:
          args: will not be used
          kwargs: a dictionary for an existing instance

        """

        date_formatter = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, date_formatter)
                setattr(self, key, value)

    def save(self):
        """
        Updates the updated_at attribute:
        with new current date and time
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary with all
        keys and values of the __dict__
        """
        instance_dictionary = self.__dict__.copy()
        instance_dictionary['__class__'] = self.__class__.__name__
        instance_dictionary['created_at'] = self.created_at.isoformat()
        instance_dictionary['updated_at'] = self.updated_at.isoformat()
        return instance_dictionary

    def __str__(self):
        """
        Returns string representation of the class and instance
        """
        return f"[{type(self).__name__}] ({self.id}) {str(self.__dict__)}"
