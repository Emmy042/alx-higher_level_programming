#!/usr/bin/python3

class Rectangle:
    """Represents a rectangle with width and height."""
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        
    def __del__(self):
        """deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
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
            return ""
        return "\n".join(str(self.print_symbol) * self.__width for _ in range(self.__height))

        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)
    
    def __repr__(self):
        """Return a string that recreates the object using eval()."""
        return f"Rectangle({self.width}, {self.height})"
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() > rect_2.area():
            return rect_1
        
        elif rect_1.area() == rect_2.area():
            return rect_1
        
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance where width and height are equal to size."""
        return cls(size, size)