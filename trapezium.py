"""
@Author: Ayuta
Description: code for drawing trapezium
"""

#logic for first triangle of trapezium
for i in range(1,11):
    for j in range(1,i):
        print("*",end=" ")
    print() 

#logic for square in middle of trapezium
for ii in range(1,10):
    for jj in range(1,10):
        print("*",end=" ")
    print()

#logic for second triangle of trapezium    
for iii in range (10,0,-1):
    for jjj in range (iii,1,-1):
        print("*",end=" ")
    print()
    