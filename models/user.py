#!/usr/bin/python3

"""User class"""

from models.base_model import BaseModel


class User(BaseModel):

    """Represent a User.
    Attributes:
        email type string: email of the users
        password string data type: password of the user.
        first_name string data type: The first name of the user.
        last_name : The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
