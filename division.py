"""
@Author: Ayuta
Description: given any positive integer n, 
print all the positive integers upto n 
divisible by 3 or 5 
Input: a positive integer
Output: positive numbers upto n
which are divisible by 3 or 5
"""

num1 = int(input("enter your number --> "))
count = 1

while count <= num1:
    if count % 3==0 or count % 5==0:
        print(count)
    count+=1
        
print("----------------------")