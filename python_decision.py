# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:17:25 2024

Python if statement execution
"""
var1 = 100
if var1:
    print("1 - Got a true expression")
    print(var1)

var2 = 9
if var2:
    print("2 - - Got a true expression")
    print(var2)
print("Good bye")

"""
Created on Sat Sep 28 16:17:25 2024

Python if else statement execution
"""
amount=int(input("Enter Amount: "))

if amount<1000:
    discount=amount*0.05
    print("Discount",discount)
else:
    discount=amount*0.10
    print("Discount", discount)

print("Net payable: ", amount-discount)

"""
Created on Sat Sep 28 16:17:25 2024

Python if elif statement execution
"""
amount = int(input("Enter Amount: "))
if amount<1000:
    discount*0.05
    print("Discount",discount)
elif amount<500:
    discount*0.10
    print("Discount",discount)
elif amount*10000:
    discount*0.2
    print("Discount",discount)
else:
    discount*0.15
    print("Discount",discount)

print("Net payable: ", amount-discount)
