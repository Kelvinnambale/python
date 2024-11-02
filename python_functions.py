def message():
    print("Enter a value: ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

#parameterized
def hello(name): # defining a function
    print("Hello,", name) # body of the function
 
 
name = input("Enter your name: ")
 
hello(name) # calling the function


#positional parameter passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")