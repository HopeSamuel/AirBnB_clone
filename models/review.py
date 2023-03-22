#!/usr/bin/python3
"""
Review Representation module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent a Review
    Inherit from base model
    """

    place_id = ""
    user_id = ""
    text = ""
