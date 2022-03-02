#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, line):
        'Programme output function'
        return exit(1)

    def do_EOF(self, line):
        'Programme output function'
        return exit(1)

    def do_all(self, line):
        if self.__class__.__name__:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
