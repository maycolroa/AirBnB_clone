#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd


"""Module that cointains class HBNB"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __class_l = ['BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review']

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
        class_l = {"BaseModel": BaseModel(), "User": User(), "State": State(),
                   "City": City(), "Amenity": Amenity(), "Place": Place(),
                   "Review": Review()}
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
        if not len(arg):
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.__class_l:
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
        if not len(arg):
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.__class_l:
            print(arg[0])
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        string = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()
        if string in objects.keys():
            objects.pop(string)
            storage.save()

    def do_all(self, arg):
        """Print all instances"""
        class_l = ["BaseModel", 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']
        new_list = []
        objects = storage.all()
        if len(arg) == 0:
            for key, value in objects.items():
                new_list.append(value.__str__())
            print(new_list)
        if len(arg) > 0:
            arg = arg.split()
            if arg[0] in class_l:
                for key, value in objects.items():
                    if key.startswith(arg[0]):
                        new_list.append(value.__str__())
                print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """method to update an instance"""
        arg = arg.split()
        if not len(arg):
            print("** class name missing **")
            return
        if len(arg) > 5:
            print("** Just one instance can be update at the time **")
            return
        if arg[0] not in HBNBCommand.__class_l:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        string = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()
        if string in objects.keys():
            setattr(objects[string], arg[2], arg[3])
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
