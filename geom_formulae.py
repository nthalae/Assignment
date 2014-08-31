__author__ = 'emmanuel'

from numbers import Number
from numpy import *


def circle_circumference(radius : Number) -> Number:
    """
    work out the circumference of a circle from the radius
    @param radius: the radius of the circle
    @return: parameter (unit from the radius)
    >>> circle_circumference(6)
    37.7
    """
    return 2*pi*radius
print (circle_circumference(6))


def circle_area(radius : Number) -> Number:
    """
    calculate the area of a circle from radius
    @param radius: the circle's radius
    @return: the parameter (unit^2 from the radius unit)
    >>> circle_area(7)
    154
    """
    return pi*radius*radius
print (circle_area(7))


def triangle_area (base : Number, height : Number) -> Number:
    """
    find the area of a triangle given the base and perpendicular height.
    @param base: base of the triangle
    @param height: height of the triangle
    @return: parameter(unit^2 from base unit)
    >>> triangle_area(16, 7)
    56
    """
    return base*height/2
print (triangle_area (16, 7))


def cone_area(radius : Number, height : Number) -> Number:
    """
    calculate the area of a cone from radius and height given in the same unit
    @param radius: the circle's radius
    @param height: the cicle's height
    @return: parameters (unit^2 from radius)
    >>> cone_volume(3, 4)
    75.4
    """
    return (pi*radius*radius)+(pi*radius*(sqrt(radius*radius+height*height)))
print (cone_area(3, 4))


def cone_area(radius : Number, height : Number, length : Number) -> Number:
    """
    calculate the area of a cone from radius, height and length given all in the same unit
    @param radius: radius of the cone
    @param height:perpendicular height of the cone
    @param length:slanting length of the cone
    @return: parameter (unit^2 from radius)
    >>> cone_area(3, 4, 5)
    75.4
    """
    return (pi*radius*radius)+(pi*radius*length)
print (cone_area(3, 4, 5))


def cube_area(side : Number) -> Number:
    """
    find the area of a cube given its side.
    @param side: length of the side of the cube
    @return: parameter (unit^2 from side)
    >>> cube_area(3.5)
    73.5
    """
    return (6*side*side)
print (cube_area(3.5))

def cube_volume(side : Number) -> Number:
    """
    work out the volume of a cube from the length of its side.
    @param side: side length of the cube
    @return: parameter (unit^3 from the length side)
    >>> cube_volume(4)
    64
    """
    return (side*side*side)
print (cube_volume(4))

def rectangle_area(length : Number, width : Number) -> Number:
    """
    calculate the area of a rectangle with length and width in the same unit
    @param length: length of the rectangle
    @param width: width of the rectangle
    @return: parameter (unit^2 from length)
    >>> ractangle_area(11, 7)
    77
    """
    return length*width
print (rectangle_area(11, 7))

def sphere_volume(radius : Number) -> Number:
    """
    calculate the volume of a cone fom aradius
    @param radius: radius of the cone
    @return: parameter (unit^3 from the radius)
    >>> sphere_volume(3)
    113.1
    """
    return (4*pi*radius*radius*radius)/3
print (sphere_volume(3))


def pyramid_volume(length : Number, width : Number, height : Number) -> Number:
    """
    calculate the volume of a pyramid from the length, width, and height.
    @param length: length of the pyramid
    @param width: width of the pyramid
    @param height: height of the pyramid
    @return:parameter (unit^3 from length)
    >>> pyramid_volume(8, 3, 7)
    56
    """
    return (length*width*height/3)
print (pyramid_volume(8, 3, 7))


def rightsquarepyramid_area(side : Number, height : Number) -> Number:
    """
    calculate the area of a right square-based pyramid from its side and height.
    :param side: side length of the pyramid base
    :param height: height of the pyramid
    :return: paramiter (unit^2 from the side)
    >>> rightsquarepyramid_area(5, 7)
    99.3
    """
    return (side*side)+ 2*side*sqrt((side*side/4)+height*height)
print (rightsquarepyramid_area(5, 7))



def ellipsoid_volume (radius1 : Number, radius2 : Number, radius3 : Number) -> Number:
    """
    calculate the volume of an ellipsoid from its radius1, radius2 and radius3)
    @param radius1: radius1 of the ellipsoid
    @param radius2: radius2 of the ellipsoid
    @param radius3: radius3 of the ellipsoid
    :return: parameter (unit^3 from radius1)
    >>> ellipsoid_volume (6, 3, 7)
    528
    """
    return 4*pi*radius1*radius2*radius3/3
print (ellipsoid_volume(6, 3, 7))

