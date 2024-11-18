#!/usr/bin/python3
""" User Class (child class of BaseModel) """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If attributes passed viakwags, init them
         if kwargs:
            if 'email' in kwargs:
                self.email = kwargs['email']
            if 'password' in kwargs:
                self.password = kwargs['password']
            if 'first_name' in kwargs:
                self.first_name = kwargs['first_name']
            if 'last_name' in kwargs:
                self.last_name = kwargs['last_name']
