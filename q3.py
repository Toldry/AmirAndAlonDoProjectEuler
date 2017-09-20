#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
import math

n = 600851475143

def isPrime(m):
    for i in range(2, math.floor(math.sqrt(m))):
        if(m%i==0):
            return False
    return True

def findSmallestFactor(m):
    for i in range(2, int(math.sqrt(m))):
        if(m%i==0):
            return i
    return m


while(True):
    sf = findSmallestFactor(n)
    print(sf)
    if(sf == n):
        break
    n = n//sf

print(n)
    

# Solution: 6857
