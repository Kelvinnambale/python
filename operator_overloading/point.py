"""
The Point class defines two private attributes __x and __y which represent x and y coordinates in a plane. Then it defines getter and setter methods for those attributes. It also defines, get_position() and move() method to get the current position and change coordinates respectively.

In line 35, we have overloaded + operator for the Point class. The __add__() method creates a new Point object by adding individual coordinates of one Point object to another Point object. Finally, it returns the newly created object to it's caller. This allows us to write expressions like:

p3 = p1 + p2
where p1, p2 and p3 are three Point objects.

Python interprets the above expression as p3 = p1.__add__(p2), and calls the __add__() method to add two Point objects. The return value from the __add__() method is then assigned to p3. It is important to note that when __add__() method is called, the value of p1 is assigned to the self parameter and the value of p2 is assigned to the point_obj parameter. The rest of the special methods works in the similar fashion.
"""
import math

class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y   

    # get the x coordinate
    def get_x(self):
        return self.__x

    # set the x coordinate
    def set_x(self, x):
        self.__x = x

    # get the y coordinate
    def get_y(self):
        return self.__y

    # set the y coordinate
    def set_y(self, y):
        self.__y = y

    # get the current position
    def get_position(self):
        return self.__x, self.__y

    # change x and y coordinate by a and b
    def move(self, a, b):
        self.__x += a
        self.__y += b

    # overloading + operator
    def __add__(self, point_obj):
        return Point(self.__x + point_obj.__x, self.__y + point_obj.__y)

    # overloading - operator
    def __sub__(self, point_obj):
        return Point(self.__x - point_obj.__x, self.__y - point_obj.__y)

    # overloading < operator
    def __lt__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) < math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)

    # overloading <= operator
    def __le__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) <= math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)

    # overloading > operator
    def __gt__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) > math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)

    # overloading >= operator
    def __ge__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) >= math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)

    # overloading == operator
    def __eq__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) == math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)

    ## overriding __str__ function
    def __str__(self):
        return "Point object is at: (" + str(self.__x) + ", " + str(self.__y) + ")"


p1 = Point(4, 6)
p2 = Point(10, 6)

print("Is p1 < p2 ?", p1 < p2)   # p1 < p2 is equivalent to p1.__lt__(p2)
print("Is p1 <= p2 ?", p1 <= p2)  # p1 <= p2 is equivalent to p1.__le__(p2)
print("Is p1 > p2 ?", p1 > p2)   # p1 > p2 is equivalent to p1.__gt__(p2)
print("Is p1 >= p2 ?", p1 >= p2)   # p1 >= p2 is equivalent to p1.__ge__(p2)
print("Is p1 == p2 ?", p1 == p2)   # p1 < p2 is equivalent to p1.__eq__(p2)

p3 = p1 + p2  # p1 + p2 is equivalent to p1.__add__(p2)
p4 = p1 - p2  # p1 - p2 is equivalent to p1.__sub__(p2)

print()  # print an empty line
print(p1)  # print(p1) is equivalent to print(p1.__str__())
print(p2)  # print(p2) is equivalent to print(p2.__str__())
print(p3)  # print(p3) is equivalent to print(p3.__str__())
print(p4)  # print(p4) is equivalent to print(p4.__str__())