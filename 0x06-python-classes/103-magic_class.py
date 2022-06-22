#!/usr/bin/python3
"""Definition of the Magic Class"""
import math


class MagicClass:
    """Defines a circle"""
    def __init__(self, radius):
        """Initialization of the magic class

        Args:
            radius (int): radius of a circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Calculates the area of a cirle
        Returns:
            Returns the area of circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumfrence of a cricle

        Returns:
            Returns the circumfrence of a circle
        """
        return (2 * math.pi) * self.__radius
