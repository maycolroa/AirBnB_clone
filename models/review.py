#!/usr/bin/python3

from lib2to3.pytree import Base
from models.base_model import BaseModel
"""Module contains review class inherits
    from base.
"""


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
