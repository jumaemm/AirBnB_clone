#!/usr/bin/env python3
"""This program implements the console loop for the AirBnB clone project"""

from models import storage
from models.base_model import BaseModel
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

    def do_default():
        pass

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
        arg_list = [i for i in line.split(" ")]
        instances = self.storage.all().values()
        if len(arg_list) == 1:
            print([str(inst) for inst in instances])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(inst) for inst in instances])

    def do_update(self, line):
        if (line == "" or line is None):
            print("** class name missing **")
            return
        rex = r'^(\w+)\s([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})\s(\w+)\s(\S+)$'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
        elif classname not in CLASSES:
            print("** class doesn't exist **")
        classname = match.group(1)
        uuid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        value = value.strip('\"')
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
                setattr(storage.all()[key], attribute, value)
                self.storage.save()

    def do_EOF:
        """EOF signal"""
        print("")
        return True

    def do_quit(self, line):
        """Quit the loop/exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
