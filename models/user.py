#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
