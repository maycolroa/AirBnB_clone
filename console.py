#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
import cmd, os, json


"""Module that cointains class HBNB"""

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # ----- basic HBNB commands -----
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """program exit with EOF"""
        exit()

    def emptyline(self):
        """allows new line"""
        pass

    def do_create(self, arg):
        """command create a new instance"""
        class_l = {"BaseModel": BaseModel()}
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg not in class_l:
            print("** class doesn't exist **")
            return
        else:
                obj = class_l.get(arg)
                storage.new(obj)
                storage.save()
                print(obj.id)

    def do_show(self, arg):
        """Command that  the string representation of an
        instance based on the class name and id
        """
        arg = arg.split()
        class_l = ['BaseModel']
        if not len(arg):
            print("** class name missing **")
            return
        if arg[0] not in class_l:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        string = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()
        if string in objects.keys():
            print(objects[string])
            
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Command to delete an instance with its class
        name and id
        """
        arg = arg.split()
        class_l = ['BaseModel']
        if not len(arg):
            print("** class name missing **")
            return
        if arg[0] not in class_l:
            print(arg[0])
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        string = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()
        if string in objects:
            objects.pop(string)
            storage.save()


        
if __name__ == '__main__':
    HBNBCommand().cmdloop()