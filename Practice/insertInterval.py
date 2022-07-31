"""
given the intervals and a new interval, insert another interval...
"""

n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]
newInterval = [int(x) for x in input().split()]
new_start, new_end = newInterval[0], newInterval[1]
op = []
def insertInterval():

    # Sort the array
    arr.sort(key = lambda  i :[ i[0]])

    i = 0
    # Insert the prev intervals where its start value is less than new interval's start value
    while i < n and arr[i][0] < new_start:
        op.append(arr[i])
        i += 1

    # then insert the new interval if no merging
    if len(op) == 0 or op[-1][1] < new_start:
        op.append(newInterval)
    # if merging, set the end of op to max of both
    else:
        op[-1][1] = max(op[-1][1], new_end)

    # then insert the remaining intervals
    while i < n:
        # if merging, set to max end
        if op[-1][1] >= arr[i][0]:
            op[-1][1] = max(op[-1][1], arr[i][1])
        else:
            op.append(arr[i])
        i += 1

    print(op)

insertInterval()