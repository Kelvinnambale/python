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