
def calHash(s, power, mod, k):

    initHash, hashMod = calculateHashOfStr(s[:k], power, mod)

    print(initHash)

    print(((initHash - getCharVal(s[0])) // power), power ** k-1 , getCharVal(s[k]), s[k])


    print(((initHash - getCharVal(s[0])) // power) + (power ** k-1) * getCharVal(s[k-1]))
    # for i in range(1, len(s)-k):
    #
    #     originalVal = (initHash // power) - getCharVal(s[i-1])
    #
    #     pass





def getCharVal( chr):
    return ord(chr) - 96

def calculateHashOfStr(s, p, m):
    print(s)
    hashVal = 0
    for i in range(len(s)):
        charVal = getCharVal(s[i])

        currVal = charVal * (p ** i)

        hashVal += currVal

    return hashVal, hashVal % m

calHash('abcde', 2, 2, 3)


