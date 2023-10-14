#!/usr/bin/python3
"""
Defines the HBNBCommand class
"""

import cmd
import models
import re
from shlex import split
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def parse(line):
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(line)]
        else:
            lexer = split(line[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(line[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class
    Defines the HBNB command interpreter
    """

    __classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
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

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, line):
        """
        Creates a new BaseModel instance,
        saves it to the JSON file,
        and prints the id
        """

        if not line:
            print("** class name missing **")
            return
        args = parse(line)
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
            args = parse(line)
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
            args = parse(line)
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
        args = parse(line)
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
        args = parse(line)
        obj_dict = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in obj_dict:
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) >= 4:
            obj = obj_dict[f"{args[0]}.{args[1]}"]
            if args[2] in obj.__class__.__dict__.keys():
                obj.__dict__[args[2]] = self.convert_to_dest_type(
                        args[3], obj.__class__.__dict__[args[2]])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) is dict:
            obj = obj_dict[f"{args[0]}.{args[1]}"]
            changes = eval(args[2])
            for k, v in changes.items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        models.storage.save()

    def do_count(self, line):
        """Counts the number of instances of a class"""

        count = 0
        args = parse(line)
        for obj in models.storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
