#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class. Has a size"""
    def __init__(self, size=0):
        """Initialize Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            str = '#' * self.__size
            for x in range(self.__size):
                print(str)
