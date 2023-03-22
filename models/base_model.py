"""Base Model Class
   The Base class of all other model
"""
import copy
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Called when a BaseModel is created"""

        if len(kwargs):
            for key, value in kwargs.items():
                val = value
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = copy.deepcopy(self.created_at)
        models.storage.new(self)

    def __str__(self):
        """String representation of Base Model"""
        return "[" + self.__class__.__name__ + \
            "] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """Updates the public attribute updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of dict"""
        temp = self.__dict__.copy()

        temp['__class__'] = self.__class__.__name__
        temp['updated_at'] = self.updated_at.isoformat()
        temp['created_at'] = self.created_at.isoformat()
        return temp
