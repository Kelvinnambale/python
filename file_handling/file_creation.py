f = open("employee.txt", "w")

f.write("First Line \n")
f.write("Second Line \n")
f.write("Third Line \n")

print("Last line", file=f)
print("Last line", file=f)

f.close()