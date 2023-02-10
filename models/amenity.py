#!/usr/bin/python3
"""Amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel

    Attributes:
        name (str): empty string for name of the amenity
    """
    name = ""
