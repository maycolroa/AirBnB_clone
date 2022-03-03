#!/usr/bin/python3
from abc import ABC, abstractmethod
from datetime import datetime 
import uuid

"""This module contain a base model that have
"""

class BaseModel(ABC):
    """Class that defines a BaseModel atributtes"""

    def __init__(self, *args, **kwargs):
        """created a new instance"""

        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                        self.__dict__)
        
    def save(self):
        self.update_at = datetime.now()
        
    def to_dict(self):
        return_dictionary = self.__dict__.copy()
        return_dictionary.update({'created_at': self.created_at.isoformat(),
                                  'update_at': self.update_at.isoformat(),
                                  '__class__': type(self).__name__})
        return return_dictionary
