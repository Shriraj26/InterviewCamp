"""
Basic Merge Interval
"""

n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]

def mergeInterval():

    newArr = []

    # sort the array based on first elem
    arr.sort(key =  lambda i:i[0])

    prev_start = arr[0][0]
    prev_end = arr[0][1]

    for i in range(1, len(arr)):
        interval = arr[i]

        # if there is overlapping
        if prev_end > interval[0]:
            prev_end = max(prev_end, interval[1])
        else:
            newArr.append([prev_start, prev_end])
            prev_start = interval[0]
            prev_end = interval[1]

    newArr.append([prev_start, prev_end])

    print(newArr)


mergeInterval()
