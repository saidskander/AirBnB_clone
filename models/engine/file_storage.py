#!/usr/bin/python3
"""class that serializes instances to a JSON file
   and deserializes JSON file to instances"""
import json
import os.path
from os import path
from models.base_model import BaseModel


class FileStorage():
    """class to serialize and deserialize classes and json strings"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public instance method to return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as outfile:
            newdict = {}
            for k, v in FileStorage.__objects.items():
                newdict[k] = v.to_dict()
            json.dump(newdict, outfile)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                temp = json.load(json_file)
                newdict = {'BaseModel': BaseModel,
                           }
                for k, v in temp.items():
                    model = k.split('.')
                    FileStorage.__objects[k] = newdict[model[0]](**v)
