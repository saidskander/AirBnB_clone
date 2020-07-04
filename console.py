#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json

"""
my_class = {"BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review}

"""


class HBNBCommand(cmd.Cmd):
    """ Command hbnb Class """

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
