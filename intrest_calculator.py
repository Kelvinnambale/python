# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:05:32 2024

@author: ADMIN
"""

print("******Intrest program calculator")

principal=int(input("Enter the Principal Amount: "))
rate=int(input("Enter the rate: "))
time=int(input("Enter the time / period: "))

print("Principal: ",principal)
print("Rate: ",rate)
print("Time: ",time)

intrest=(principal*(rate/100)*time)

print("Intrest: ", intrest)