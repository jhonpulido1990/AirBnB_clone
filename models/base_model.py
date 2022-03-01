#!/usr/bin/python3
from datetime import datetime
from time import strftime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs and len(kwargs) is not 0:
            del kwargs['__class__']
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        if args is not None:
            pass

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
        dic.update({'created_at' : self.created_at.isoformat(), 'updated_at' : self.updated_at.isoformat()})
        return(dic)
