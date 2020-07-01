#!/usr/bin/python3
"""AIRBNB project Base module"""
import uuid
import datetime
import models


class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initialization method"""
        if kwargs:
            if "created_at" not in kwargs.keys():
                raise Exception("fail create")
            if "updated_at" not in kwargs.keys():
                raise Exception("fail update")
            if "id" not in kwargs.keys():
                raise Exception("fail id")
            for x, y in kwargs.items():
                if x == '__class__':
                    pass
                else:
                    setattr(self, x, y)
            self.created_at = datetime.datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """update updated_at/datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary updated/created"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict

    def __str__(self):
        """return the representation of the Basemodel inztance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)
