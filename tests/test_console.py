#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
import json
from io import StringIO

class TestHBNBCommand_prompt(unittest.TestCase):
    """
    Tests for the HBNB 
    command prompt
    """

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", my_output.getvalue().strip())

class TestHBNBCommandHelp(unittest.TestCase):
    """
    Tests for help message in HBNB
    """
    def test_help(self):
        expected_output = ("Documented commands (type help <topic>):\n"
                           "=======================================\n"
                           "EOF all clear create destroy help quit show update")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(self.cmd_instance.onecmd("help"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_commmand(self, command, expected_output):
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(self.cmd_instance.onecmd("help {}".format(command)))
            self.assertEqual(expectes_output, my_output.getvalue().strip())

    def test_help_quit(self):
        expected_output = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_EOF(self):
        expected_output = "ctrl-D to exit program"
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNCommand().onecmd("help EOF"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_create(self):
        expected_output = ("Creates a new instance :\n"
                           "Usabe: create <class name>")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_destroy(self):
        expected_output = ("Deletes an instance\n"
                           "Usage: destroy <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_show(self):
        expected_output = ("Prints the string representation of an instance\n"
                           "Usage: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help show:"))
            self.assertEqual(expected_output, my_output.getvalur().strip())

    def test_help_all(self):
        expected_output = ("Prints all string representation of all\n"
                           "instances based or not on the class name\n"
                           "Usage1: all\n"
                           "Usage2: all <class name>")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help All"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_update(self):
        expected_output = ("Updates an instance by adding or updating attribute\n"
                           "Usage: update <class name> <id> <attribute name> \"<attribute value>\"")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(expected_output, my_output.getvalye().stript())


class ConsoleTest(unittest.TestCase):
    """
    Test Error
    """
    def check_json(self, classname, id):
        key_n = classname+"."+id
        with open(self.fl_path, 'r') as fl:
            my_data = json.load(fl)
        self.assertIn(key_n, my_data)
        self.assertEqual(my_data[key_n]["id"], id)
        self.assertEqual(my_data[key_n]["__class__"], classname)

    def test_error(self):
        com_classname = ["create", "update", "show", "destroy"]
        com_id = ["update", "show", "destroy"]
        com_attr = ["update"]

