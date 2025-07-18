#!/usr/bin/python3

class Rectangle:
    """Represents a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value
      
    @height.setter
    def height(self, value):
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value   
        
        
    def area(self):
        
        return self.__width * self.__height
    
    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        
        if self.width == 0 or self.height == 0:
            return 0
        
        return 2 * (self.__width + self.__height)
    
    
    def __str__(self):
        """Returns a string representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""  # empty string if no area

        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)
    
    def __repr__(self):
        """Return a string that recreates the object using eval()."""
        return f"Rectangle({self.width}, {self.height})"