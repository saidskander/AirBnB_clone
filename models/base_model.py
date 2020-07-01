#!/usr/bin/python3
"""AIRBNB project Base module"""
import uuid
import datetime
import models


class BaseModel:
    """ BaseModel class rbnb project """

    def __init__(self, *args, **kwargs):
        """ Init method """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "my_number":
                    self.my_number = kwargs.get(key)
                if key == "name":
                    self.name = kwargs.get(key)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """update updated_at/datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary updated/created"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()
        return mydict

    def __str__(self):
        """return the representation of the Basemodel inztance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)
