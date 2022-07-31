"""
This is one of the most neat techniques to count the number of ones or number of bits in the number!!!
The way we do is we always drop the least significant bit that is the last bit that is 1
loop and remember this formula!!!!

X = X & (X - 1)

and loop till X does not become 0 and increment the counter too..

This is an optimization technique that runs till num reaches 0 and us half than counting ones while shifting
the num to right

"""



def countOnes(num):

    count = 0
    while num != 0:
        num = num & (num - 1)
        count += 1

    return count



print(countOnes(10))
print(countOnes(32))
print(countOnes(5))
print(countOnes(19))

print(getLSB((21)))