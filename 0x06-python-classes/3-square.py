#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Square Initialization
        Args:
            size - represents the size of the square defined
            Area - represents the area of the square defined
        Raises:
            TypeError - if size is not an integer
            ValueError - if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Finds the area of a square
        Returns: Area of the square
        """
        return (self.__size * self.__size)
