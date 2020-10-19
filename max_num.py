"""
@Author: Ayuta
Description: find the largest of three given integers
Input: three user given integers 
Output: Largest of the given three integers
"""
# taking input from user:
num1=int(input("please enter your first number >> "))
num2=int(input("please enter your second number >> "))
num3=int(input("please enter your third number >> "))

# finding out the max number:
if (num1 >= num2):
    if (num1 >= num3):
        print(num1,"is the greatest number")
    else:
        print(num3,"is the greatest number")
else:
    if (num2 >= num3):
        print(num2,"is the greatest number")
    else:
        print(num3,"is the greatest number")