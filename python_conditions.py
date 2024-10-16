# Read two numbers
number1 =int(input("Enter the first number: "))
number2 =int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)


first_no =int(input("Enter the first number: "))
second_no =int(input("Enter the second number: "))
third_no =int(input("Enter the third number: "))

largest_no = first_no

if second_no > largest_no:
    largest_no = second_no

if third_no > largest_no:
    largest_no = third_no
    
print("Largest number: ", largest_no)