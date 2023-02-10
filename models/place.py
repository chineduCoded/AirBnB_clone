#!/usr/bin/python3
"""Place moodule"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel

    Attributes:
        city_id (str): empty string for city_id of the place
        user_id (str): empty string for user_id of the place
        name (str): empty string for name of the place
        description (str): empty string for description of the place
        number_rooms (int): 0 for number of rooms of the place
        number_bathrooms (int): 0 for number of bathrooms of the place
        max_guest (int): 0 for max number of guests the place can accommodate
        price_by_night (int): 0 for price per night for the place
        latitude (float): 0.0 for latitude of the place
        longitude (float): 0.0 for longitude of the place
        amenity_ids (list): empty list for the list of amenity ids later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
