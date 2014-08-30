__author__ = 'emmanuel'

from numbers import Number
from numpy import *

def circle_area(radius : Number) -> Number:
    """
    calculate the area of a circle from radius
    @param radius: the circle's radius
    @return: the parameter (unit^2 from the radius)
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
    >>> cone_volume(3, 4)
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

def sphere_volume(radius : Number) -> Number:
    """
    calculate the volume of a cone fom aradius
    :param radius: radius of the cone
    :return: parameter (unit^3 from the radius)
    >>> sphere_volume(3)
    113.1
    """
    return (4*pi*radius*radius*radius)/3
print (sphere_volume(3))

def pyramid_volume(length : Number, width : Number, height : Number) -> Number:
    """
    calculate the volume of a pyramid from the length, width, and height.
    :param length: length of the pyramid
    :param width: width of the pyramid
    :param height: height of the pyramid
    :return:parameter (unit^3 from length)
    >>> pyramid_volume(8, 3, 7)
    56
    """
    return (length*width*height/3)
print (pyramid_volume(8, 3, 7))


def pyramid_area(length : Number, width : Number, height: Number) -> Number:
    """
    calculate the area of a pyramid from the length, width, and height.
    :param length: length of the pyramid
    :param width: width of the pyramid
    :param height: height of the pyramid
    :return: parameter (unit^2 from length)
    >>> pyramid_area (8, 3, 7)
    105.46
    """
    return (length*width)+length*sqrt(width*width/4)+width*sqrt((length*length/4)+(height*height))
print (pyramid_area(8, 3, 7))


def ellipsoid_volume (radius1 : Number, radius2 : Number, radius3 : Number) -> Number:
    """
    calculate the volume of an ellipsoid from its radius1, radius2 and radius3)
    :param radius1: radius1 of the ellipsoid
    :param radius2: radius2 of the ellipsoid
    :param radius3: radius3 of the ellipsoid
    :return: parameter (unit^3 from radius1)
    >>> ellipsoid_volume (6, 3, 7)
    528
    """
    return 4*pi*radius1*radius2*radius3/3
print (ellipsoid_volume(6, 3, 7))

