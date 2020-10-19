"""
@Author: Ayuta
Description: multiplication table of any given number
Input: any positive integer 
Output: multiplication table upto 10x of input
"""
num = int(input("please enter your number --> "))
count = 1

while (count < 11):
    print(num, "x", count, "=", num*count)
    count += 1
    
else:
    print("______________________________")