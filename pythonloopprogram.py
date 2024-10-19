fname = str(input("Enter the Username: "))
passwd = str(input("Enter the Password: "))
counter= 3
if passwd == "admin":
    print("Username: ", fname)
    print("Password", passwd)
else:
    while passwd != "admin":
        while counter !=0:
            print("Wrong password")
            passwd=str(input("Enter password again: "))
            counter-=1            
        print("Contact system administrator")
        

print("Username: ", fname)
print("Password", passwd)