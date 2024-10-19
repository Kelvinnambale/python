"""
    replace continue, pass to demonstrate.
"""
for letter in 'python':
    if letter=='h':
        continue
    print('Current letter: ',letter)
var=10
while var>0:
    print('Current variable value: ',var)
    var= var-1
    if  var == 5:
        continue
print('Goodbye')

"""Break example"""
for i in range(1,6):
    if i==3:
        break
    print("Inside the loop")
print("Outside the loop")

#Continue example
print("\nContinue Instruction")
for i in range(1,6):
    if i==3:
        continue
    print("inside the loop")
print("Outside the loop")


#break statement 2
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")