"""
je zero ahet te 1 kar ani je 1 te 0 .. this is the flip bits thing
1. To Flip bits, ex-or it with one!!
    Ex - 1011 exor 1111 -- 0100
    if u want u can flip only the bits that u want that is -
    1011 if u want to flip last 2 blits, then u can ex-or with one that is only at last 2 bits that is -
    1011 exor 0011 --- 1000

"""


def flipBit(num):
    return num ^ 1


print(flipBit(5))
