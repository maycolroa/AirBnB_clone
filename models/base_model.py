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

    def __str__(self):
        string = ""
        string = "[{}] ({}) {}".format(type(self).__name__, self.id, self.created_at)
        return string
        
        
        
    

base = BaseModel()
print(base.id)
base2 = BaseModel()
print(base2.id)
print(base.created_at)

print(base)