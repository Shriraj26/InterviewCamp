"""
Basic implementation of fibonacci without using DP

"""

def fibo(n):

    # base case - if n == 0 and if n == 1
    if n == 0 or n == 1:
        return n

    return fibo(n-1) + fibo(n-2)

n = int(input('enter a number '))

print(fibo(n))





