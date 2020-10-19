"""
@Author: Ayuta
Description: find the largest of three given integers
Input: three user given integers 
Output: Largest of the given three integers
"""
num = int(input("enter an integer --> "))
max_num = num

while (num != -1):
    num = int(input("enter another integer --> "))
    if (num > max_num):
        max_num=num
        
print(max_num,"is the greatest number")
    
