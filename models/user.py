#!/usr/bin/python3

"""Moodule that contain user class inherits from
    base class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""