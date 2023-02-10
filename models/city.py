#!/usr/bin/python3
"""City moodule"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel

    Attributes:
        state_id (str): empty string for state_id of the city
        name (str): empty string for name of the city
    """
    state_id = ""
    name = ""
