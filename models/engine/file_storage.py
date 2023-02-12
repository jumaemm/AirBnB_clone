#!/usr/bin/python3
"""
Stores dictionary representation in JSON format,
for easy readability
"""
import json 
from models.base_model import BaseModel

class FileStorage:
    """Converts dictionary representation to a JSON string.
    
    Attributes:
        __file_path(str): File to save to
        __objects (dict): objects dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary representation"""
        return self.__objects
    def new(self, obj):
        """sets the obj with the key in __objects"""
        if (obj):
            self.__objects["{}.{}".format(type(obj).__name__, obj.id] = obj
    
    def save(self):
        """serializes objects to JSON file"""
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                ob = json.load(file)
                for key in ob:
                    self.__objects[key] = classes[ob[key]["__class__"]](**ob[key])
    except:
        pass
