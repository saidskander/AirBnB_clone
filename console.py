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

    def do_EOF(self, arg):
        "EOF command to exit the program"
        return True

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        pass

        def emptyline(self):
        pass

    def do_create(self, arg):
        "Create command to create a new instance"
        if not arg:
            print("** class name missing **")
        elif arg in my_class:
            for key, value in my_class.items():
                if key == arg:
                    new_instance = my_class[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        "Delete an instance on the class name and class id"
        main_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif main_arg[0] not in my_class:
            print("** class doesn't exist **")
        elif len(main_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = main_arg[0] + "." + main_arg[1]
                try:
                    my_objects.pop(my_key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                    print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
