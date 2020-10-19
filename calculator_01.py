# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:10:43 2020

@author: Ayutasouri

calculator
Ver 1.0
"""

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("please select an operation code:")
print("press 1 to add")
print("press 2 to subtract")
print("press 3 to multiply")
print("press 4 to divide")

while True:
    choice=input("please enter your choice \n")
    num1=float(input("please enter the first number \n"))
    num2=float(input("please enter the second number \n"))
    
    if choice=="1":
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=="2":
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice=="3":
        print(num1,"x",num2,"=",multiply(num1,num2))
    elif choice=="4":
        print(num1,"÷",num2,"=",divide(num1,num2))
    else:
        print("give a valid math operation you retard!!")
      
      
           