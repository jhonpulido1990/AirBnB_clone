#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
from models import storage

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

        elif len(line) == 0:
            print ("** class name missing **")

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        if len(line) == 0:
           print("** class name missing **")
        else:
           line2 = line.split()
           if line2[0] == "BaseModel" and len(line2) == 1:
               print("** instance id missing **")
           elif line2[0] != "BaseModel":
               print("** class doesn't exist **")
           else:
               basem = "{}.{}".format(line2[0], line2[1])
               if basem in storage.all().keys():
                   print(storage.all()[basem])
               else:
                   print("** no instance found **")

    def do_destroy(self, line):
        if len(line) == 0:
            print("** class name missing **")
        else:
            line2 = line.split()
            if line2[0] == "BaseModel" and len(line2) == 1:
                print("** instance id missing **")
            elif line2[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                basem = "{}.{}".format(line2[0], line2[1])
                if basem in storage.all().keys():
                    del storage.all()[basem]
                    storage.save()
                else:
                    print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
