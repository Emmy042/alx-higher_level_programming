#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """rectangle class that inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """return width"""
        return self.__width
    
    @property
    def height(self):
        """return height"""
        return self.__height
    
    @property
    def x(self):
        """return x"""
        return self.__x
    @property
    def y(self):
        """return y"""
        return self.__y
    
    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @y.setter
    def y(self,y):
        """sets y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        
    @x.setter
    def x(self,x):
        """sets x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        
        
    def area(self):
        """gets the area of a rectangle"""
        return self.width * self.height
    
    def display(self):
        """return the rectangle instance with #"""
        # for i in range(self.width):
        #     print('#' * self.width)
        # Print vertical offset (y) first
        for _ in range(self.y):
            print()
    
    # Then print each row of the rectangle with horizontal offset (x)
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
         """Assigns arguments to attributes in order: id, width, height, x, y"""
         attrs = ["id", "width", "height", "x", "y"]
    
         if args and len(args) > 0:
          for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
         else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
        