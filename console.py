#!/usr/bin/python3
"""hello fixed """
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models import storage

my_class = {"BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Command HBNB Class for HBNB project """

    prompt = "(hbnb) "
    file = None

    def EOF(self, arg):
        "EOF command to exit the program"
        return True

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
