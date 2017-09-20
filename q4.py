# -*- coding: cp1252 -*-
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def RevNum(n):
    m=0
    while(n!=0):
        m=m*10+n%10
        n//=10
    return m

def IsPal(n):
    return (RevNum(n)==n)

def getLargestPal(d):
    n=10**d -1
    while(n>=100):
        m=n
        while(m>=100):
            mul = n*m
            if(IsPal(mul)):
                return (n,m,mul)
            m-=1
        n-=1

def getLargestPal(d):
    n=10**d -1
    length = 1
    diag = True
    i = n
    j = n
    while(True):
        k = i
        l = j
        for h in range(1,length + 1):
            mul = l * k
            if(IsPal(mul)):
                return (mul, l, k)
            k -= 1
            l += 1
        if(diag):
            i-=1
            diag = False
        else:
            j-=1
            diag = True
            length +=1
        
result = getLargestPal(3)
print("The largest palindrom is {0}, and it is a product of {1} and {2}".format(result[0], result[1], result[2]))



# Solution: 906609
