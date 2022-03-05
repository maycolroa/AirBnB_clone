#!/usr/bin/python3
"""Module that contains class FilesStorage"""
import json
import os


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
        if obj is not None:
            self.__objects.update(
                {str(type(obj).__name__ + "." + obj.id): obj})

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)
        """
        new_dict = {}
        if self.__objects is not None:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
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

        deserialized = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as file:
                contents = file.read()

        else:
            return
        if contents is not None:
            deserialized = json.loads(contents)
            for key, value in deserialized.items():
                if key not in self.__objects.keys():
                    new_obj = eval(value["__class__"])(**value)
                    self.new(new_obj)
        else:
            pass
