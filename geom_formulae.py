__author__ = 'emmanuel'

from numbers import Number
from numpy import *

def circle_area(radius : Number) -> Number:
    """
    calculate the area of a circle from radius
    @param radius: the circle's radius
    @return: the parameter (same unit as the radius)
    >>> circle_area(7)
    154
    """
    return pi*radius*radius
print (circle_area(7))


def cone_area(radius : Number, height : Number) -> Number:
    """
    calculate the area of a cone from radius and height given in the same unit
    :param radius: the circle's radius
    :param height: the cicle's height
    :return: the parameters (unit^2 from radius)
    >>> cone_area(3, 4)
    75.4
    """
    return (pi*radius*radius)+(pi*radius*(sqrt(radius*radius+height*height)))
print (cone_area(3, 4))

def cone_area(radius : Number, height : Number, length : Number) -> Number:
    """
    calculate the area of a cone from radius, height and length given all in the same unit
    :param radius: radius of the cone
    :param height:perpendicular height of the cone
    :param length:slanting length of the cone
    :return: the area (unit^2 from radius)
    >>> cone_area(3, 4, 5)
    75.4
    """
    return (pi*radius*radius)+(pi*radius*length)
print (cone_area(3, 4, 5))

def rectangle_area(length : Number, width : Number) -> Number:
    """
    calculate the area of a rectangle with length and width in the same unit
    :param length: length of the rectangle
    :param width: width of the rectangle
    :return: parameter (unit^2 from length)
    >>> ractangle_area(11, 7)
    77
    """
    return length*width
print (rectangle_area(11, 7))

