"""
You are given a sorted array of intervals, insert a new interval into it!!
1. Till the start of new interval is less than the current interval, insert the intervals into the output
2. Then insert the new interval, merge if necessary
3. Then add the remaining intervals
"""
n = int(input('Enter the number of intervals'))
arr = [[int(y) for y in input().split()] for x in range(n)]
print('INsert new interval')
newInterval = [int(x) for x in input().split()]
finalArr = []

def insertInterval():

    new_start, new_end = newInterval
    op = []
    i = 0

    # insert all the intervals before the new intervals
    while i < n and new_start > arr[i][0]:
        op.append(arr[i])
        i += 1

    # insert the new interval

    # if there is no merging or the output is still empty insert the interval as it is
    if not op or op[-1][1] < new_start:
        op.append([new_start, new_end])
    # else change the op of the last elem to max of the one ends
    else:
        op[-1][1] = max(op[-1][1], new_end)

    # add other intervals, merge with the last ops if needed
    while i < n:

        # if there is no merging, add as it is
        if op[-1][1] < arr[i][0]:
            op.append(arr[i])
        else:
            op[-1][1] = max(op[-1][1], arr[i][1])
        i += 1
    return op


print(insertInterval())