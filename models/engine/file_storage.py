#!/usr/bin/python3
"""provide file storage class"""
import json
import os.path
from os import path
from models.base_model import BaseModel


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
        """reload JSON file if it exixt"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                temp = json.load(json_file)
                new_dict = {'BaseModel': BaseModel,
                            }
                for x, y in temp.items():
                    model = x.split('.')
                    FileStorage.__objects[x] = new_dict[model[0]](**y)
