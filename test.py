
print("Python Syntax and first program")
print("Hello world")

print("Python Indentation")
if 5 > 2:
	print("Five is greater than 2")

print("Python variable")
x=str(3)
z=int(3)
y=float(3)

print(x)
print(z)
print(y)

#Get type Function
a=3
b="John"

print(type(a))
print(type(b))

#Python Variables
"""x = "awesome"

def myfunc():
	print("Python is " + x)
myfunc()
"""

#Global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

  myfunc()

print("Python is " + x)


#python numbers
c=1
d=2.0
e=1j

print(type(c))
print(type(d))
print(type(e))

#type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
