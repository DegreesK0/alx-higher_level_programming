#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Square Initialization
        Args:
            size - represents the size of the square defined
        Raises:
            TypeError - if size is not an integer
            ValueError - if size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Finds the area of a square
        Returns: Area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with character #
        """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
