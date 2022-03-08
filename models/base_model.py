#!/usr/bin/python3
"""
    Class that defines a Base model
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
        Class that defines Base model attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """
            Create new instances according given arguments and store the info
        """
        if kwargs:
            for key, value in kwargs.items():

                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            Modify the stdr output with a specific format
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
            Update the attribute updated_at with the current datetime
            and save changes in json file.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            Return a Dictionary with specific attributes and format
        """
        representation = self.__dict__.copy()
        representation["updated_at"] = self.updated_at.isoformat()
        representation["created_at"] = self.created_at.isoformat()
        representation["__class__"] = self.__class__.__name__
        return representation
