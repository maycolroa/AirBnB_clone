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
        args = args
        kwargs = kwargs
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                        self.__dict__)
        
    def save(self):
        self.update_at = datetime.now()
        
    def to_dict(self):
        return "{}".format(self.__dict__)

base = BaseModel()
print(base.to_dict)