#!/usr/bin/python3
"""
This module contain a base model that have
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Class that defines a BaseModel atributtes
    """
    def __init__(self, *args, **kwargs):
        """
        created a new instance
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """
        instance that return str of class atributtes
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        update the update atributte
        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance:
        """
        return_dictionary = self.__dict__.copy()
        return_dictionary.update({'created_at': self.created_at.isoformat(),
                                  'update_at': self.update_at.isoformat(),
                                  '__class__': type(self).__name__})
        return return_dictionary
