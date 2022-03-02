#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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

    def do_create(self, line):
        if line == "BaseModel":
            Nline = BaseModel()
            print(Nline.id)
            Nline.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
