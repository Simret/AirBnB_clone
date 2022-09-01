#!/usr/bin/python3
''' This Modules is designed to define all attributes, intasces and functions for all other classes'''
import uuid
from datetime import datetime
import models


class BaseModel():
    ''' This class is base model for airBnB console project'''
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            timeformat = "%Y-%m-%dT%H:%M:%S.%f"
            for k, val in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(val, timeformat)
                else:
                    self.__dict__[k] = val

    def __str__(self):
        '''string formating function'''
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
