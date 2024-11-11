import math
class rectangle():
    def __init__(self, color, filled, width, length):
        self.__color = color
        self.__filled = filled
        self.__width = width
        self.__length = length

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled
    
    def set_filled(self, filled):
        self.__filled = filled
    
    def get_area(self):
        return self.__width * self.__length 
    
    def get_perimeter(self):
        return 2 (self.__width + self.__length)

class circle():
    def __init__(self, color, filled, radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius      

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_area(self):
        return math.pi * self.__radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.__radius