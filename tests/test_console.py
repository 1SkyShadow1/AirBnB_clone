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
                "========================================\n"
                "EOF  all  clear  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_quit(self):
        expected_output = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_EOF(self):
        expected_output = "Ctrl-D to exit the program"
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_create(self):
        expected_output = ("Creates a new instance")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_destroy(self):
        expected_output = ("Deletes any instance")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_show(self):
<<<<<<< HEAD
        expected_output = ("Print the string representation of an instance\n"
                "Usage: show <class name> <id>")
=======
        expected_output = ("Prints the string representation of an instance\n"
                           "Usage: show <class name> <id>")
>>>>>>> 42e05ed291423046b9a51da6cfe74293a6b2f675
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_all(self):
<<<<<<< HEAD
        expected_output = ("Prints all string representation of all "
                "instances based or not on the class name\n"
                "Usage1: all\n"
                "Usage2: all <class name>")
=======
        expected_output = ("Prints all string representation of all\n"
                           "instances based or not on the class name\n"
                           "Usage1: all\n"
                           "Usage2: all <class name>")
>>>>>>> 42e05ed291423046b9a51da6cfe74293a6b2f675
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(expected_output, my_output.getvalue().strip())

    def test_help_update(self):
        expected_output = ("Updates an instance by adding or updating attribute\n"
                "Usage: update <class name> <id> <attribute name> \"<attribute value>\"")
        with patch("sys.stdout", new=StringIO()) as my_output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(expected_output, my_output.getvalue().strip())


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

        """ class name missing """
        for com in com_classname:
            # print(f"class name missing : {com}")
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(com)
                self.assertCountEqual(expected, f.getvalue().strip())

                """class doesn't exist"""
                class_dont_exist = ["create x", "update x",
                        "show x", "destroy x", "all x"]
                for com in class_dont_exist:
                    # print(f"class doesn't exist : {com}")
                    with patch('sys.stdout', new=StringIO()) as f:
                        expected = "** class doesn't exist **"
                        HBNBCommand().onecmd(com)
                        self.assertCountEqual(expected, f.getvalue().strip)

                """intance id missing """
                cmds = ["update", "show", "destroy"]
                all_class = HBNBCommand().all_class
                for cmd in cmds:
                    for clas in all_class:
                        # print(f"instance id missing : {com} {clas}")
                        with patch('sys.stdout', new=StringIO()) as f:
                            expected = "** instance id missing **"
                            HBNBCommand().onecmd(f"{com} {clas}")
                            self.assertCountEqual(expected, f.getvalue().strip())
                """ no instance found"""
                cmds ["update", "show", "destroy"]
                all_class = HBNBCommand().all_class
                wrong_id = "x"
                for cmd in cmds:
                    for clas in all_class:
                        # print(f"no instance found : {com} {clas} {wrong_id}")
                        with patch('sys.stdout', new=StringIO()) as f:
                            expected = "** no instance found **"
                            HBNBCommand().onecmd(f"{com} {clas} {wrong_id}")
                            self.assertCountEqual(expected, f.getvalue().strip())

             def test_create_object(self):
                 """ testing for create """
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd("create BaseMmodel"))
                    Key = "BaseModel.{}".format(output.getvalue().strip())
                    self.assertIn(Key, storage.all().keys())
                with patch("sys.stdout", newStringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd("create User"))
                    Key = "User.{}".format(output.getvalue().strip())
                    self.assertIn(()Key, storage.all().keys())
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd("create State"))
                    Key = "State.{}".format(output.getvalue().strip())
                    self.assertIn(Key, storage.all().key())
                with patch("sys.stdout", newStringIO()) as output:
                    self.assertFals(HBNBCommand().onecmd("create City"))
                    Key = "City.{}".format(output.getvalue().strip())
                    self.assertIn(Key, storage.all().keys())
                with patch("sys.stdout", new=StringIO()) as output:
                    selfassertFalse(HBNBCommand).onecmd("create Place")
                    Key = "Place.{}".format(output.getvalue().strip())
                    self.assetIn(Key, storage.all().keys())
                with patch("sys.stdout", newStringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                    Key = "Amenity.{}".format(output.getvalue().strip())
                    self.assertIn(Key, storage.all().keys())
                with patch("sys.stdut", new=StringIO()) as output:
                    self.assetFalse(HBNBCommand().onecmd("create Review"))
                    Key = "Review.{}".format(output.getvalue().strip())
                    self.assertIn(Key, storage.all().keys())

                    """ value missing """
                    new_BaseModel = BaseModel()
                    new_User = User()
                    new_State = State()
                    new_City = City()
                    new_Amenity = Amenity()
                    new_Place = Place()
                    new_Review = Review()
                    id_BaseModel = new_BaseModel.id
                    id_User = new_User.id
                    id_State = new_State.id
                    id_City = new_City.id
                    id_Amenity = new=Amenity.id
                    id_Place = new_Place.id
                    id_Review = new_Review.id
                    id_dict = {"BaseModel": id_BaseModel, "User": id_User, "State": id_State, "City": id_City, "Amenity": id_Amenity, "Place": id_Place, "Review":}
                    cmds = ["update"]
                    all_class = HBNBCommand().all_class
                    for cmd in cmds:
                        for clas in all_class:
                            #print(f"no instance found : {cmd} {clas} {wrong_id}")
                            #print(f"{cmd} {clas} {id_dict[clas]}")
                            with patch('sys.stdout', new=StringIO()) as f:
                                expected = "** value missing **"
                                HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name")
                                self.assertCountEqual(expected, f.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
