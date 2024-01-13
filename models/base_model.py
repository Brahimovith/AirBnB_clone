#!/usr/bin/python3
"""la classe BaseModel"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

         Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k,v in kwargs.items():
                if k != "__class__":
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, k, v)
        models.storage.new(self)
    def __str__(self):
        """string print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """save objects"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """to _ dict """
        r = self.__dict__.copy()
        r['__class__'] = self.__class__.__name__
        r['created_at'] = self.created_at.isoformat()
        r['updated_at'] = self.updated_at.isoformat()
        return r
