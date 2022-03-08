#!/usr/bin/python3
"""
Class that defines FileStorage
"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
        Initialize private FileStorage class attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the __objects dictionary
        """
        return(self.__objects)

    def new(self, obj):
        """
            Creates a new key(class.id) & value(instance attributes dictionary)
            of an instance in __objects dictionary
        """
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Append all keys & values set on __objects dictionary
            into a new dictionary to save all instances in a json file
        """
        dict_serialized = {}
        savedict = {}
        for key, value in FileStorage.__objects.items():
            savedict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(savedict))

    def reload(self):
        """
            Load the .json file(verify existence), set all keys & values into
            the __objects dictionary and recreate instances found in the file
        """
        dictReload = {}
        try:
            cls_arr = {"BaseModel": BaseModel, "Amenity": Amenity,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State, "User": User}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                dictReload = json.load(file)
                for key, value in dictReload.items():
                    cls_to_ins = cls_arr.get(value['__class__'])
                    obj = cls_to_ins(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
