#!/usr/bin/python3
"""
Defines the HBNBCommand class
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class
    Defines the HBNB command interpreter
    """

    def __init__(self):
        """ Creates an HBNBCommand instance"""
        super().__init__()
        self.prompt = "(hbnb)"

    def do_EOF(self, line):
        """End of File command
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
