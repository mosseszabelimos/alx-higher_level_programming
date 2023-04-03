#!/usr/bin/python3
"""9-rectangle, project 0x08 task 9.
"""


class Rectangle:
    """Class for printing or computation of dimensions of a rectangle.
    Takes in args for width and height of a rectangle, and contains methods
    for calculation of the area or perimeter, and for creating a square by
    making a new instance of equal sides. __str__, __repr__, and __del__
    fuctionality defined below.
    Attributes:
        number_of_instances (int): counter incrementing for every
            instantiation, and decrementing for every instance deletion.
        print_symbol (str): single character to be used in assembling string
            representation of rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.
        Args:
            width (int): horizontal dimension of rectangle, defaults to 0
            height (int): vertical dimension of rectangle, defaults to 0
        """
        type(self).number_of_instances += 1
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.
        Returns:
            __width (int): horizontal dimension of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle
        Attributes:
            __width (int): horizontal dimension of rectangle
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.
        Returns:
            __height (int): vertical dimension of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle
        Attributes:
            __height (int): vertical dimension of rectangle
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.
        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle
        Returns:
            Area of rectangle: __width * __height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`
        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle
        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
        (__height * 2).
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print the rectangle
