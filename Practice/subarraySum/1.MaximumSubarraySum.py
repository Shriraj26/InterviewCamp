arr = [int(x) for x in input().split()]

def maxSumSubarray():

    maxTillI = arr[0]
    maxEver = arr[0]

    for i in range(1, len(arr)):

        maxTillI = max(maxTillI + arr[i], arr[i])

        maxEver = max(maxEver, maxTillI)

    return maxEver

print(maxSumSubarray())

