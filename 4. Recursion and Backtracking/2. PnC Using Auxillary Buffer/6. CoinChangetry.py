"""
Need to do this again....
Given a set of coin denominations, print out the different ways you can make a target amount. You can use as many coins of each denomination as you like.

For example: If coins are [1,2,5] and the target is 5, output will be:

[1,1,1,1,1]

[1,1,1,2]

[1,2,2]

[5]
"""

bufferArr = []

arr = [int(x) for x in input().split()]
target = int(input())

def coinVariations(n, target, subArr):


    # base case aditya verma
    if n == 0 or target == 0:
        return subArr

    ans = []
    # include a coin
    if arr[n-1] <= target:
        subArr.append(arr[n-1])

        ans1 = coinVariations(n-1, target - arr[n-1], subArr)
        ans2 = coinVariations(n, target - arr[n-1], subArr)

        for i in ans1:
            print('ans1 ',i, end = ' ')
            ans.append(i)
        print()
        for i in ans2:
            print('ans2 ',i, end = ' ')
            ans.append(i)
        print()
    else:
        ans3 = coinVariations(n-1, target, subArr)
        for i in ans3:
            print('ans3 ',i, end = ' ')
            ans.append(i)
        print()
    return ans

print(coinVariations(len(arr), target, []))