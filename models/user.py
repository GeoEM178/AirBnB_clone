#!/usr/bin/python3
"""
Module: user.py
This is the "user model" module.
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """User extend from base model

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
