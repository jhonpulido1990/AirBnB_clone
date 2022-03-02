#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:

    __file_path = "file.json"
    __objects = "{}.id".format(id.__class__.__name__)
    
    def all(self):
        return self.__objects

    def new(self, obj):
        objecti = "{}.id".format(id.__class__.__name__)[obj]
        self.__objects = objecti
    
    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dumps(self.__objects(f.write))

    def reload(self):
        with open(self.__file_path, 'r') as f:
            self.__objects = json.dumps(f.read)