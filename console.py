#!/usr/bin/python3
"""
Difinition of
AirBnB console
model
"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):
    """
    Definition for
    AirBnB console
    class
    """
    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    valid_int_attributes = ["number_rooms", "number_bathrooms",
                            "max_guest", "last_name"]

    valid_float_attributes = ["latitude", "longitude"]

    valid_string_attributes = ["name", "amenity_id", "place_id",
                               "state_id", "user_id", "city_id",
                               "description", "text", "email",
                               "password", "first_name", "last_name"]

    def do_create(self, arg):
        """
        Create new instance
        """
        av_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
                }
        if self.valid(arg):
            my_args = arg.split()
            if arg[0] in av_classes:
                storage.save()
                print(av_classes[args[0]]().id)

    def valid_arg(self, arg, my_id=False, my_attr=False):
        """
        Validates arguments passed
        """
        my_args = arg.split()
        args_len = len(arg.split())
        if args_len == 0:
            print("** class name missing **")
            return (False)
        elif my_args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return (False)
        elif args_len < 2 and my_id:
            print("** instance id missing **")
            return (False)
        elif my_id and my_args[0]+"."my_args[1] not in storage.all():
            print("** no instance found **")
            return (False)
        elif args_len == 2 and my_attr:
            print("** attribute name missing **")
            return (False)
        elif args_len == 3 and my_attr:
            print("** value missing **")
            return (False)
        return (True)

    def emptyline(self):
        """
        Does nothing
        when empty lin  e
        recieved
        """
        pass

    def do_EOF(self, arg):
        """
        Enables
        ctrl-d to exit
        program
        """
        return (True)

    def do_quit(self, arg):
        """
        Exits the program
        """
        return (True)

    def do_destroy(self, arg):
        """
        Deletes any instance
        """
        if self.valid(arg, True):
            my_args = arg.split()
            my_key = my_args[0]+"."+my_args[1]
            del storage.all()[my_key]
            storage.save()

    def do_clear(self, arg):
        """
        Clears the data
        stored
        """
        storage.all().clear()
        self.do_all(arg)
        print("** Data has been cleared! **")

    def do_show(self, arg):
        """
        prints the string form
        of an instance
        """
        if self.valid(arg, True):
            my_arg = arg.split()
            my_key = my_args[0]+"."+my_args[1]
            print(storage.all()[_key])
