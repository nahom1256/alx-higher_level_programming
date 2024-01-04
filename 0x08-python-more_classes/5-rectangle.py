#!/usr/bin/python3
"""Defines a Rectangle """


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width (int): The width.
            height (int): The height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must bger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the heiangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height m be an integer")
        if value < 0:
            raise ValueError("hmust be >= 0")
        self.__height = value

    def area(self):
        """Return he Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the ter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return tpresentation of the Rectangle.

        Rngle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the stringn of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Preletion of a Rectangle."""
        print("Bye rectangle...")
