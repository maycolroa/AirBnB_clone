#!/usr/bin/python3
from models.base_model import BaseModel
"""Module that contain city class inherits
    from base.
"""


class City(BaseModel):
    """Class define basic data of City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
