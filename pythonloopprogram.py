fname = str(input("Enter the Username: "))
passwd = str(input("Enter the Password: "))
count= 1
if passwd == "admin":
    print("Username: ", fname)
    print("Password", passwd)
else:
    while passwd != "admin":
        print("Wrong password")
        passwd=str(input("Enter password again: "))
print("Username: ", fname)
print("Password", passwd)