"""
You are given an array of intervals, merge into a single one...
First and foremost, sort the array based on the first index
There are 2 cases -
1. If there is an overlap - end > interval[0]
    end will be max(end, interval[1])
2. else if there is no overlap -
    add the first interval, update start and end to point to next intervals
    add the second interval too
We append to the new array only when there is no merging!!! Look into the code u will get this
"""

n = int(input('Enter the number of intervals'))
arr = [[int(y) for y in input().split()] for x in range(n)]
finalArr = []
def mergeInterval():

    arr.sort(key=lambda i: i[0])

    start = arr[0][0]
    end = arr[0][1]

    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        interval = arr[i]

        # if there is merging, set the end to max of init end and next end of interval
        if end >= interval[0]:
            end = max(end, interval[1])
        # Else
        else:
            finalArr.append([start, end])
            start = interval[0]
            end = interval[1]

    finalArr.append([start, end])

    return finalArr


print(mergeInterval())