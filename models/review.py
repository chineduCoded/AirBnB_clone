#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel

    Attributes:
        place_id (str): empty string for place_id of the review
        user_id (str): empty string for user_id of the review
        text (str): empty string for the text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
