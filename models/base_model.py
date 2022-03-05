#!/usr/bin/python3
"""
    Module contain class basemodel
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
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary with specific attribbites and format
        """
        new_dict = self.__dict__.copy()
        new_dict.update({'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat(),
                         '__class__': type(self).__name__})
        return new_dict
