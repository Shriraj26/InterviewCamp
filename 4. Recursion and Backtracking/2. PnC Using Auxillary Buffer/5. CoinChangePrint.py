"""Given a set of coin denominations, print out the different ways you can make a target amount. You can use as many coins of each denomination as you like.

For example: If coins are [1,2,5] and the target is 5, output will be:

[1,1,1,1,1]

[1,1,1,2]

[1,2,2]

[5]

To Remember -
1. Buffer madhe taak
2. Sagle fn calls ghe, i repeat hou shakta mhanun haath nako lavu, total vadhav ani i tasach thev
3. total equal zala jitka required ahe tr print kar
"""

bufferArr = []

arr = [int(x) for x in input().split()]
target = int(input())


def coinVariations(total, startIndex):
    if total > target:
        return

    # base case - if total == target then we return
    if total == target:
        print(bufferArr)
        return

    for i in range(startIndex, len(arr)):
        # Add the element to the buffer
        bufferArr.append(arr[i])

        # Give me all possible combinations using this number, note her that we haven't incremented i this means
        # repetitions are allowed
        coinVariations(total + arr[i], i)

        # After my work, pop the elem from the buffer and move to next elem in the array in the loop
        bufferArr.pop()


coinVariations(0, 0)
