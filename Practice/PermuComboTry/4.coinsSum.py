"""
1 2 5 and if sum is 5 -- how many combinations can u make
"""


arr = [int(x) for x in input().split()]
total = int(input())
buffArr = []


def coinsMagic(k):

    if k > total:
        return

    if k == total:
        print(buffArr)
        return


    for i in range(len(arr)):

        buffArr.append(arr[i])

        coinsMagic(k + arr[i])

        buffArr.pop()


coinsMagic(0)