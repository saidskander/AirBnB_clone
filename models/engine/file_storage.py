#!/usr/bin/python3
""" provide file storage class """
import json
import os.path
from os import path
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage():
    """class of FileStorage json strings format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary FileStorage __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """create new instance"""
        key = "{}.{}".format(obj.__class__.
                             __name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save the function."""
        with open(FileStorage.__file_path, "w") as File:
            new_dict = {}
            for x, y in FileStorage.__objects.items():
                new_dict[x] = y.to_dict()
            json.dump(new_dict, File)

    def reload(self):
        """reload from JSON File only if it exixt"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as File:
                temp = json.load(File)
                new_dict = {'BaseModel': BaseModel,
                            'User': User,
                            'Amenity': Amenity,
                            'City': City,
                            'State': State,
                            'Place': Place,
                            'Review': Review}
                for x, y in temp.items():
                    model = x.split('.')
                    FileStorage.__objects[x] = new_dict[model[0]](**y)
