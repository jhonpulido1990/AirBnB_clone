#!/usr/bin/python3
'''
module import: cmd, json, shlex, models,
BaseModel, User, State, City, Amenity,
Place, Review, Storage
'''
import cmd
import json
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

DICTT = {'BaseModel': BaseModel(), 'User': User(), 'State': State(),
         'City': City(), 'Amenity': Amenity(), 'Place': Place(),
         'Review': Review()}


class HBNBCommand(cmd.Cmd):
    '''
    functions that call methods
    '''
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'Quit command to exit the program\n'
        return True

    def do_all(self, line):
        if len(line) == 0:
            lista = []
            for key, value in storage.all().items():
                lista.append(value.__str__())
            print(lista)
            return

        ln = line.split()
        if ln[0] in DICTT:
            lista2 = []
            for key, value in storage.all().items():
                if ln[0] == value.to_dict()["__class__"]:
                    lista2.append(value.__str__())
            print(lista2)
            return
        else:
            print("** class doesn't exist **")
            return

    def do_create(self, line):
        if line in DICTT:
            Nline = DICTT[line]
            print(Nline.id)
            Nline.save()

        elif len(line) == 0:
            print("** class name missing **")

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        if len(line) == 0:
            print("** class name missing **")
        else:
            line2 = line.split()
            if line2[0] in DICTT and len(line2) == 1:
                print("** instance id missing **")
            elif line2[0] not in DICTT:
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
            if line2[0] in DICTT and len(line2) == 1:
                print("** instance id missing **")
            elif line2[0] not in DICTT:
                print("** class doesn't exist **")
            else:
                basem = "{}.{}".format(line2[0], line2[1])
                if basem in storage.all().keys():
                    del storage.all()[basem]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, line):
        if len(line) == 0:
            print("** class name missing **")
        else:
            ln = shlex.split(line)
            if ln[0] not in DICTT:
                print("** class doesn't exist **")
            elif ln[0] in DICTT and len(ln) == 1:
                print("** instance id missing **")
            elif ln[0] in DICTT and len(ln) == 2:
                basem = "{}.{}".format(ln[0], ln[1])
                if basem in storage.all().keys():
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            elif ln[0] in DICTT and len(ln) == 3:
                print("** value missing **")
            elif ln[0] in DICTT and len(ln) == 4:
                basem = "{}.{}".format(ln[0], ln[1])
                if basem in storage.all().keys():
                    ln2 = storage.all()[basem]
                    ln2.to_dict()
                    setattr(ln2, ln[2], ln[3])
                    ln2.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
