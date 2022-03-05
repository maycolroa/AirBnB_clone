#!/usr/bin/python3
from lib2to3.pytree import Base
from models.base_model import BaseModel
"""
    Module contains review class inherits
    from base.
"""


class Review(BaseModel):
    """
        Class that defines rewiew
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
