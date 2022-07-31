"""
1. Swap ith and jth bits -
    Initially, get the ith and jth bit by the get and set bits function that we have written earlier
    then, if both are equal, no need to swap, else
    Create a mask of 1 and then exor it, or shift 1 << i and 1 << j
    take or of both these - 1<<i | 1 << j
    then exor it with our num
    ans -- num ^ ((1 << i) | ( 1 << j))

"""

def getIthBit(num, i):
    return (num >> i) & 1

def swapithandJthBits(num, i, j):

    if getIthBit(num, i) != getIthBit(num, j):
        return num ^ ((1 << i) | (1 << j))
    else:
        return num


print(swapithandJthBits(14, 0, 3))
