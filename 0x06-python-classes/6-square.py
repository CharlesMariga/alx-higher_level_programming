#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (int, int): Coordinates of the new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size property

        Args:
            value (int): The size of the new square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retries the position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position property
        Args:
            value (int): The new coordinates for the square.
        """
        if (not isinstance(value, tuple) or
                len != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num > -1 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the are of a square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(0, self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for x in range(0, self.__position[0])]
                [print("#", end="") for j in range(0, self.__size)]
                print()
