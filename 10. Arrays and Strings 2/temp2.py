import math




def convertToBin(num):
    return bin(num)

def convertToNum(b):
    return int(b, 2)

def countOnesFunc(num):
    num = str(num)
    count = 0
    for i in num:
        if i == '1':
            count += 1
    return count


def Log2(x):
    return math.log10(x) / math.log10(2)


def checkPowerOf2(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))


countOnes = [0]



def getValAfterOp(num, countOnes, q):

    if num % 2 == 0:

        if checkPowerOf2(num):
            # add
            if q == 1:
                countOnes[0] += 1
        else:
            pass

    else:
        if checkPowerOf2(num+1):
            pass
        else:
            pass


    # cases
    # check if the number is even
    # if the num is power of 2
    # add -- just increase
    # sub - num ones ins remaiing zeroes
    # else
    # add -- just increase
    # sub remainis same

    # if the num is odd
    # if the num is 1 less than 2 power --
    # add - num zeroes is the num ones
    # sub - 1 less than the num ones

    pass

def getOnes(s, q, num):

    res = []

    # get the num, and num ones initially
    num[0] = convertToNum(s)

    countOnes[0] = countOnesFunc(num[0])
    res.append(countOnes[0])



    for i in q:
        if i == 1:
            # call func
            getValAfterOp(num[0], countOnes[0], 1)
            num[0] += 1

        else:
            getValAfterOp(num[0], countOnes[0], 2)
            num[0] -= 1


s = input()
q = [1,2,2,1]
num = [0]
getOnes(s, q)



