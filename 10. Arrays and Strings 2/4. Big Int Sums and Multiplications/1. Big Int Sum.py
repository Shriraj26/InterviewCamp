"""
Given 2 arrays of digits, calculate the sum of both
Find the larger and smaller elem, then append zeroes to the smaller element till smaller becomes
length becomes equal to larger length then carry is 0 initially, this is just like the integer sum that
u did in school, keep adding larger and smaller and then update carry... thats it

"""


a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
res = [None] * (max(len(a), len(b))+1)

def getSum(a, b):

    larger = a if len(a) > len(b) else b
    smaller = a if larger == b else b

    # resize smaller to add zero to it
    while len(smaller) != len(larger):
        smaller = [0] + smaller

    print(larger, smaller)

    carry = 0
    for i in range(len(larger)-1, -1, -1):
        sum = carry + larger[i] + smaller[i]
        carry = sum // 10
        res[i+1] = sum % 10

    res[0] = carry

    print(res)


    pass

getSum(a, b)