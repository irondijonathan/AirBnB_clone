#!/usr/bin/python3
"""
Defines the FileStorage class
"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """

        try:
            with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(FileStorage.__objects))
        except Exception:
            pass

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                json_str = f.read()
                FileStorage.__objects = json.loads(json_str)
        except Exception:
            pass
