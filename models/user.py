#!/usr/bin/python3
"""User Module to represent an User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
        Public attrs:
            email: str
            password: str
            firstname: str
            last_name: str
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
