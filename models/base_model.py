#!/usr/bin/python3
"""
Defines the BaseModel class
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Creates a BaseModel instance
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """
        Returns the string representation of an instance
        """

        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        Contains an extra key __class__,
        that contians the class name of the object.
        """

        dict2 = self.__dict__.copy()
        dict2["__class__"] = self.__class__.__name__
        dict2["created_at"] = str(self.created_at.isoformat())
        dict2["updated_at"] = str(self.updated_at.isoformat())

        return dict2
