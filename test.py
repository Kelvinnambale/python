"""
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

print("Python is " + x)"""

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)