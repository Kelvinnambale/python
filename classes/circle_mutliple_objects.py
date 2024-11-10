from circle import *

my_circle1 = circle(5)
my_circle2 = circle(10)
my_circle3 = circle(15)

print("Address of circle objects")
print("Address of circle 1: ", id(my_circle1))
print("Address of circle 2: ", id(my_circle2))
print("Address of circle 3: ", id(my_circle3))

print("Address of radius objects")
print("Address of circle 1: ", id(my_circle1.radius))
print("Address of circle 2: ", id(my_circle2.radius))
print("Address of circle 3: ", id(my_circle3.radius))

print("Radius of circles")
print("Radius of circle 1: ", my_circle1.radius)
print("Radius of circle 2: ", my_circle2.radius)
print("Radius of circle 3: ", my_circle3.radius)

print("Area of circles")
print("Area of circle 1: ", my_circle1.get_area())
print("Area of circle 2: ", my_circle2.get_area())
print("Area of circle 3: ", my_circle3.get_area())

print("Perimeter of circles")
print("Perimeter of circle 1: ", my_circle1.get_perimeter())
print("Perimeter of circle 2: ", my_circle2.get_perimeter())
print("Perimeter of circle 3: ", my_circle3.get_perimeter())