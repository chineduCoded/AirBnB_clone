#!/usr/bin/python3
"""Defines BaseModel Class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Handles initialization, serialization, and deserialization of instances.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the instance with an id and a created_at timestamp.

        Args:
        *args: non-keyworded arguments passed
        **kwargs: keyworded arguments passed

        Return: none
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the instance
        """
        dico = self.__dict__.copy()
        dico['__class__'] = self.__class__.__name__
        dico['created_at'] = self.created_at.isoformat()
        dico['updated_at'] = self.updated_at.isoformat()
        return dico
