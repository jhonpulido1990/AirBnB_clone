#!/usr/bin/python3
"""serialization and deserialization of your future instances"""


from datetime import datetime
import uuid
import models


class BaseModel:
    '''Create a file named models/base_model.py'''

    def __init__(self, *args, **kwargs):
        '''define of constructor'''

        if kwargs and len(kwargs) != 0:
            del kwargs['__class__']
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.updated_at = datetime.strptime(self.updated_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.strptime(self.created_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
        if args is not None:
            pass

    def __str__(self):
        '''print date'''

        return "[{:s}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        '''method that save in storage'''

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''method that create dictionary'''

        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic.update({'created_at': self.created_at.isoformat("T", "microseconds"),
                    'updated_at': self.updated_at.isoformat("T", "microseconds")})
        return dic
