#!/usr/bin/python3

"""Defines the State class."""

from models.base_model import BaseModel


class State(BaseModel):

    """Represent a state.

    Attributes:
        name string data type: It is name of the state.
    """

    name = ""
