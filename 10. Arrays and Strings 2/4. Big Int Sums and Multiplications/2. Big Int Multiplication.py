"""


"""


a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
res = [None] * (max(len(a), len(b))+1)

def getProduct(a,b):
    larger = a if len(a) > len(b) else b
    smaller = a if larger == b else b

    print(smaller, larger)

    res = [0]

    zeroesCount = 0
    # For digits of a, loop b too
    for i in range(len(smaller)-1, -1, -1):

        product = [0] * (1 + len(larger) + zeroesCount)

        carry = 0

        for j in range(len(larger)-1, -1, -1):

            p = smaller[i] * larger[j] + carry
            carry = p // 10
            product[j+1] = p % 10

        product[0] = carry

        res = getSum(product, res)

        zeroesCount += 1

    return res


def getSum(a, b):


    print('values passed to a and b ',a, b)
    larger = a if len(a) > len(b) else b
    smaller = a if larger == b else b

    res = [None] * (len(larger) + 1)
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

    return res




res = getProduct(a, b)
print(res)
k = 0
for i in range(len(res)):
    if res[i] != 0:
        break
    k += 1


print('here ',res[k:])
