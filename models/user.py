#!/usr/bin/python3

"""Moodule that contain user class inherits from
    base class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines information
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
