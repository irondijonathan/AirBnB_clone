#!/usr/bin/python3
"""
Defines the HBNBCommand class
"""

import cmd
import models
import shlex as sh
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class
    Defines the HBNB command interpreter
    """

    __classes = {
            "BaseModel": BaseModel
            }

    def __init__(self):
        """ Creates an HBNBCommand instance"""
        super().__init__()
        self.prompt = "(hbnb) "

    def do_EOF(self, line):
        """Closes the program when recieving End of File command
        """
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, line):
        """
        Creates a new BaseModel instance,
        saves it to the JSON file,
        and prints the id
        """

        if not line:
            print("** class name missing **")
            return
        args = sh.split(line)
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = self.__classes[args[0]]()
            obj.save()
            print(obj.id)

    def help_create(self):
        print("Creates a new BaseModel instance, ",
              "saves it to the JSON file, and prints the id")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        if not line:
            print("** class name missing **")
        else:
            args = sh.split(line)
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2 or args[1] == "":
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[f"{args[0]}.{args[1]}"])

    def help_show(self):
        print("Prints the string representation of",
              " an instance based on the class name and id")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if not line:
            print("** class name missing **")
        else:
            args = sh.split(line)
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2 or args[1] == "":
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[f"{args[0]}.{args[1]}"]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        objs = models.storage.all()
        if not line:
            print([str(objs[x]) for x in objs])
            return
        args = sh.split(line)
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(objs[x]) for x in objs
                  if args[0] == objs[x].__class__.__name__])

    def help_all(self):
        print("Prints all string representation of all instances ",
              "based or not on the class name.")

    def convert_to_dest_type(self, arg, dest):
        """Converts the argument to the type of its destination variable"""

        if type(dest) is str:
            return str(arg)
        elif type(dest) is int:
            return int(arg)
        elif type(dest) is float:
            return float(arg)
        else:
            return arg

    def do_update(self, line):
        """Updates an instance based on class name and id"""

        if not line:
            print("** class name missing **")
        else:
            args = sh.split(line)
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2 or args[1] == "":
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in models.storage.all():
                print("** no instance found **")
            elif len(args) < 3 or args[2] == "":
                print("** attribute name missing **")
            elif len(args) < 4 or args[3] == "":
                print("** value missing **")
            else:
                obj = models.storage.all()[f"{args[0]}.{args[1]}"]
                obj.__dict__[args[2]] = self.convert_to_dest_type(
                        args[3], obj.__dict__[args[2]])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
