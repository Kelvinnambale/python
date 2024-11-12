import os
f = os.path.isfile("/home/nams/Documents/serial.txt")

if f == True:
    s = open("/home/nams/Documents/serial.txt", "rt")
    print(s.read(1))

    s.close()
else:
    print("File doesnt exist")

