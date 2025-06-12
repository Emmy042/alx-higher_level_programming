#!/usr/bin/python3

class Base:
    """base class of all models"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initalization function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
