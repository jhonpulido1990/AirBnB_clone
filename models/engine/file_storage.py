#!/usr/bin/python3
'''
import model: BaseModel,
User, State, City, Amenity,
Place, Review, json
'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    '''serializes instances to a
    JSON file and deserializes
    JSON file totest_base_model.pyinstances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if obj is not None:
            keysi = obj.__class__.__name__ + '.' + obj.id
            self.__objects[keysi] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        dictiona = {}
        for keysi in self.__objects:
            dictiona[keysi] = self.__objects[keysi].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dictiona, f)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists) '''
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
