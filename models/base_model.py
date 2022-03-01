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
        self.created_at = self.created_at.isoformat()
        self.updated_at = datetime.isoformat(datetime.now())
        return dict((key, getattr(self, key)) for key in dir(self) if key not in dir(self.__class__))
