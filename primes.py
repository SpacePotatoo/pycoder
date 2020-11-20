"""
input: any positive integer
output: all prime numbers upto the user-specified number, starting from 1.
"""
def prime_finder(n):
    global primes
    
    primes = [True]*(n+1)
    primes[0],primes[1] = False,False
    
    for j in range (2, n+1):
        if primes[j] == False:
            continue
        else:
            for i in range(j*j, n+1, j):
                primes[i] = False
        
global primes
n = int(input("give your number\n>>"))
prime_finder(n)
print('here are your prime numbers:')
for i in range(2, n+1):
    if primes[i] == True: 
        print(i, end=', ')