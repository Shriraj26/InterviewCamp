"""
1. reverse bits of a number
    For a number, if u have 2 pointers start and end, swap first and last bits, and increment start and decremenet end,
    then u can get the ans!!

"""

def getIthBit(num, i):
    return (num >> i) & 1

def swapithandJthBits(num, i, j):

    if getIthBit(num, i) != getIthBit(num, j):
        return num ^ ((1 << i) | (1 << j))
    else:
        return num

def revbits(num):
    i = 0
    j = 31
    while i < j:
        num = swapithandJthBits(num, i, j)
        i += 1
        j -= 1


    return num

print(revbits(10))

print(revbits(2**30))

