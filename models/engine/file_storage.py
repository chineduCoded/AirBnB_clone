#!/usr/bin/python3
"""Defines FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Handles storage and retrieval of instances to and from files."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects stored."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Args:
            obj: Add a new object to the storage.
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Save all objects to the file."""
        with open(FileStorage.__file_path, mode='w+', encoding='utf-8') as f:
            to_save = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            f.write(json.dumps(to_save))

    def reload(self):
        """Deserialize JSON file to objects."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    klass = k.split(".")[0]
                    self.__objects[k] = eval(klass)(**v)
        except FileNotFoundError:
            pass
