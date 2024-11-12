f = open("employee.txt", "r")

print("First chunk:", f.read(4), end="\n\n")    # read the first 4 characters
print("Second chunk:", f.read(10), end="\n\n")  # read the next 10 character
print("Third chunk:", f.read(), end="\n\n")     # read the remaining characters 

f.close()