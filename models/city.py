#!/usr/bin/python3
"""
Module: city.py
This is the "city model" module.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City extending the BaseModel
    that represent different city of an object.

    Attributes:
        state_id: string - empty string
        name: string - empty string
    """
    state_id = ""
    name = ""
