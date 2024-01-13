#!/usr/bin/python3
"""
Module: amenity.py
This is the "amenity model" module.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by place extending base model

    Attributes:
        name: string
    """

    name = ""
