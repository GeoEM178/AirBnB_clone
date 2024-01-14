#!/usr/bin/python3
"""The Review model
This module defines the Review class.
Review for places
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """An review provided by a reviews for places

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
