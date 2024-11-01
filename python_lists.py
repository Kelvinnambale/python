

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(len(beatles)):
    beatles.append(input("Enter Stu Sutcliffe: "))
    beatles.append(input("Enter Ringo Starr: "))
print("Step 3:", beatles)

# step 4
del beatles[3]
del beatles[4]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))