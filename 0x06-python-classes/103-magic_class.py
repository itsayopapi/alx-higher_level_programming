#!/usr/bin/python3
import math


class MagicClass:
    """A circle class"""

    def __init__(self, radius=0):
        """Initialized circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return circumference of circle"""
        return 2 * math.pi * self.__radius
