#!/usr/bin/python3
"""Defines User Module"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    User class inherits from BaseModel and contains information about a user.

    Attributes:
        email (str): an empty string
        password (str): an empty string
        first_name (str): an empty string
        last_name (str): an empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
