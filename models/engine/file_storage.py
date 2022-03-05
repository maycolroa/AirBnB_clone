#!/usr/bin/python3

import json
import os

"""Module that contains class FilesStorage"""


class FileStorage():
    """class that realice serialization
    and deserealization] JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """return all the objects of dict"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id
        """
        if obj:
            self.__objects.update({str(type(obj).__name__ +
                                       "." + obj.id): obj})

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)
        """
        if self.__objects is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            with open(self.__file_path, mode="w+", encoding="utf-8") as file:
                json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        dict_deserialized = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as my_file:
                content = my_file.read()
        else:
            return
        if content is not None or bool(content) is True:
            dict_deserialized = json.loads(content)
        for key, value in dict_deserialized.items():
            if key not in self.__objects.keys():
                ClassName = value["__class__"]
                new_instance = eval("{}(**value)".format(ClassName))
                self.new(new_instance)
        else:
            pass