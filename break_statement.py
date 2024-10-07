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