#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = (uuid.uuid4()).hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        dic["updated_at"] = self.updated_at.isoformat()
        return(dic)
