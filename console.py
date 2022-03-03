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

        elif line != "BaseModel" and len(line) > 0:
            print ("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_show(self, line):
        if len(line) == 0:
           print("** class name missing **")
        else:
           line2 = line.split()
           if line2[0] == "BaseModel" and len(line2) < 1:
               print("** instance id missing **")
           elif line2[0] != "BaseModel":
               print("** class doesn't exist **")
           else:
               pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
