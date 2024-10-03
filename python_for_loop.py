"""
For loop example
"""
for var in list(range(10)):
    print(var)
"""
Python for loop example
"""
for letter in 'python':
	print("Current letter",letter)
fruits=["Banana","Apple","Orange"]
for x in fruits:
	print("I like ",x)
"""
Python iterating by sequence example
"""
for index in  range(len(fruits)):
	print("I like",fruits[index])

"""
Python iterating by using else example
"""
numbers=[11,33,56,99,63,23,43,53,97,95,105,109]
for i in numbers:
	if i%2==0:
		print("the list contain even numbers")
	break
else:
	print()