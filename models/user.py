#!/usr/bin/python3
from models.base_model import BaseModel
"""Moodule that contain user class inherits from
    base class.
"""


class User(BaseModel):
    """
        Class that defines information
        about the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
