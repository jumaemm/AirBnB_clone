#!/usr/bin/env python3
"""This program implements the console loop for the AirBnB clone project"""

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import cmd
import re

CLASSES = {
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
}


class HBNBCommand(cmd.Cmd):
    "Class representing the command interpretor"

    prompt = "(hbnb) "
    storage = storage

    def do_create(self, line):
        """Create an instance of the given class. Return it's ID
        """
        arg_list = [i for i in line.split(" ")]
        if not line:
            print("** class name missing **")
        elif arg_list[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            self.storage.save()

    def do_show(self, line):
        """Show the details of a particular instance with instance ID given
        structure: show <classname> <instance_id>
        """
        arg_list = line.split()
        if arg_list:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Destroy the instance of the given class and ID"""
        arg_list = line.split()
        if arg_list:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Show all instances; whether for a given class or in
        the entire JSON file"""
        arg_list = [i for i in line.split(" ")]
        instances = self.storage.all().values()
        if arg_list[0] == "":
            print([str(inst) for inst in instances])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(inst) for inst in instances if
                      arg_list[0] in str(inst)])

    def do_update(self, line):
        if (line == "" or line is None):
            print("** class name missing **")
            return
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return
        classname = match.group(1)
        uuid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if classname not in CLASSES:
            print("** class doesn't exist **")
        elif uuid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uuid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                value = value.strip('\"')
                setattr(storage.all()[key], attribute, value)
                self.storage.save()

    def do_EOF(self, line):
        """EOF signal"""
        print("")
        return True

    def do_quit(self, line):
        """Quit the loop/exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
