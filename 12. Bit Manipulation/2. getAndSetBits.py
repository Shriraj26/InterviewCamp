"""
1. Get ith Bit- To get ith bit,
    Shift the num right by i
    AND 1 with it

2. set ith bit to given val
    If val is 1 -
        newNum - Shift left 1 by i bits
        OR this newNum with original num
    else if the val is 0 -
        calculate the new num as above - newNum - Shift left 1 by i bits
        take ones compliment of this nuwnum
        AND this newNum with original num

"""


def getBit(num, i):
    return (num >> i) & 1


def setBits(num, i, val):
    newNum = 1 << i
    if val == 1:
        return num | newNum
    else:
        newNum = ~newNum
        return num & newNum


print(getBit(40, 3))

print(setBits(11, 0, 0))
