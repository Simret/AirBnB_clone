#!/usr/bin/python3

"""Defines the hbtn console."""

import cmd
import models
import re
from shlex import split
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
