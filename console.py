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
        "Delete class name and class id method"
        m_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif m_arg[0] not in my_class:
            print("** class doesn't exist **")
        elif len(m_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                main_keys = m_arg[0] + "." + m_arg[1]
                try:
                    my_objects.pop(main_keys)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                    print("** instance id missing **")

    def do_all(self, arg):
        "Show all instances based on class name"
        main_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif main_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                main_keys = key.split(".")
                if main_keys[0] == main_arg[0]:
                    my_list.append(str(values))
            print(my_list)

    def do_update(self, arg):
        'Update class name and class id'
        main_arg = shlex.split(arg)
        if len(main_arg) == 0:
            print("** class name missing **")
        elif len(main_arg) == 1:
            print("** instance id missing **")
        elif len(main_arg) == 2:
            print("** attribute name missing **")
        elif len(main_arg) == 3:
            print("** value missing **")
        elif main_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_objects = FileStorage.all(self)
            main_keys = main_arg[0] + "." + main_arg[1]
            flag = 0
            for key, values in my_objects.items():
                if key == main_keys:
                    flag = 1
                    my_values = my_objects.get(key)
                    setattr(values, main_arg[2], main_arg[3])
                    values.save()
            if flag == 0:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
