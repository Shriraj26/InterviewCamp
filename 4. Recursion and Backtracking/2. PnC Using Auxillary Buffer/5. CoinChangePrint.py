"""Given a set of coin denominations, print out the different ways you can make a target amount. You can use as many coins of each denomination as you like.

For example: If coins are [1,2,5] and the target is 5, output will be:

[1,1,1,1,1]

[1,1,1,2]

[1,2,2]

[5]
"""

bufferArr = []

arr = [int(x) for x in input().split()]
target = int(input())

def coinVariations(total, startIndex):

    if total > target:
        return

    #base case - if total == target then we return
    if total == target:

        print(bufferArr)
        return

    for i in range(startIndex, len(arr)):

        bufferArr.append(arr[i])
        coinVariations(total + arr[i], i)
        bufferArr.pop()

coinVariations(0, 0)