#!/usr/bin/python3
"""
Defines the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    __classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }

    def all(self):
        """
        Returns the __objects dictionary
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """

        try:
            with open(self.__file_path, "w", encoding='utf-8') as f:
                save_obj = {}
                for key in self.__objects:
                    save_obj[key] = self.__objects[key].to_dict()
                f.write(json.dumps(save_obj))
        except Exception:
            pass

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_str = f.read()
                load_obj = json.loads(json_str)
                for key in load_obj:
                    obj = load_obj[key]
                    self.__objects[key] =\
                        self.__classes[obj["__class__"]](**obj)
        except Exception as ex:
            pass
