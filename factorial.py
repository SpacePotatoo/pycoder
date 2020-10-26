"""
@Author: Ayuta
Description: find the factorial
Input: an integer 
Output: factorial of that integer
"""

input_num = int(input("enter your number --> "))
num=input_num
fact = 1

if input_num == 0:
    print("Factorial of",input_num,"= 1")
    
else:

    while num >= 1:
        fact = fact*num
        num -= 1    

    print("Factorial of",input_num,"=",fact)


 
