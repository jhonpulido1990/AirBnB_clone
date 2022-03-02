#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    def do_quit(self, line):
        return exit(1)

if __name__ == '__main__':
    HBNBCommand().cmdloop()