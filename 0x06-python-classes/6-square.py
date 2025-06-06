#!/usr/bin/python3
class Square:
    """Represents a square with a given size.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: Gets or sets the current size of the square."""
        return self.__size
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
    not all(isinstance(num, int) and num >= 0 for num in value)
):
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        area = self.__size
        return area * area
    
    def my_print(self):
        
        """Print the square using '#' and handle position."""
        
        if self.__size == 0:
            print()
            return
        
        # Print vertical space (position[1])
        for _ in range(self.__position[1]):
            print()
            
        # Print square lines with horizontal spaces (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)