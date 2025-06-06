#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Init square with size (default 0)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return area of the square."""
        area = self.__size
        return area * area
