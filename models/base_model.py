#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, created_at = datetime.now()):
        self.id = str(uuid.uuid4())
        self.created_at = created_at
        self.updated_at = datetime
        print('Instance created at', self.created_at)
        print('Instance update at', self.updated_at)
        print('Instance id', self.id)

    def __str__(self):
        '''
        print date
        '''
        return "[Basemodel] ({}) {}".format(
            self.id, self.__dict__)

    
