"""
This is different from the flip bits!! as compliment of 00110 is 00001 and not 11001 as if u do flip bits,
then all the initial zeroes are flipped too!! we just want to flip the bits after the most significant one!

So we do these steps - we need to find a mask and exor it with the number to get our flipped compliment
Steps to find the mask
1. get the most significant one by taking log of number -- int(log n) --- position where 1 starts (MSB)
2. shift number 1 towards left by the num that we got in step 1
3. subtract 1 from it

"""

import math
def getCompliment(num):

    positionOfMSB = int(math.log(num, 2))
    mask = (1 << (positionOfMSB + 1)) - 1

    return num ^ mask


print(getOnesCompliment(10))