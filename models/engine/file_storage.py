#!/usr/bin/python3
"""
File storage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Respresentation of file storage 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Adds a new object
        to __objects
        with a key in form <class name>.id
        """
        object_dict = obj.to_dict()
        object_id = object_dict["id"]
        class_name = object_dict["__class__"]
        key_name = "{}.{}".format(class_name, object_id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        Saves objects
        to a JSON file
        """
        fl_path = FileStorage.__file_path
        serialized_data = dict(FileStorage.__objects)
        for key, value in serialized_data.items():
            serialized_data[key] = value.to_dict()
        with open(fl_path, 'w') as fl:
            json.dump(serialized_data, fl)

    def reload(self):
        """
        Reloads the JSON
        objects from a
        JSON file
        """
        fl_path = FileStorage.__file_path
        serialized_data = FileStorage.__objects
        if os.path.exists(fl_path):
            try:
                with open(fl_path) as fl:
                    for key, value in json.load(fl).items():
                        if "BaseModel" in key:
                            serialized_data[key] = BaseModel(**value)
                        elif "User" in key:
                            serialized_data[key] = User(**value)
                        elif "Place" in key:
                            serialized_data[key] = Place(**value)
                        elif "State" in key:
                            serialized_data[key] = State(**value)
                        elif "City" in key:
                            serialized_data[key] = City(**value)
                        elif "Amenity" in key:
                            serialized_data[key] = Amenity(**value)
                        elif "Review" in key:
                            serialized_data[key] = Review(**value)
            except Exception:
                pass
