#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, created_at = datetime.now()):
        self.id = (uuid.uuid4()).hex
        self.created_at = created_at
        self.updated_at = created_at

    def __str__(self):
        '''
        print date
        '''
        return "[Basemodel] ({}) {}".format(
            self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["update"] = datetime.isoformat(datetime.now())
        return(dic)
