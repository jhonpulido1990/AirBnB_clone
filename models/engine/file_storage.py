#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            keysi = obj.__class__.__name__ + '.' + obj.id
            self.__objects[keysi] = obj

    def save(self):
        dictiona = {}
        for keysi in self.__objects:
            dictiona[keysi] = self.__objects[keysi].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dictiona, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except:
            pass
