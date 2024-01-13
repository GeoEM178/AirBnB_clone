#!/usr/bin/python3
"""
Module: state.py
This is the "state model" module.
"""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """State extending the BaseModel
    that represent different states of an object.

    Attributes:
        name: string - empty string
    """
    name = ""
