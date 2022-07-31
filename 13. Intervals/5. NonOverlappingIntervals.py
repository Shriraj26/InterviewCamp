"""
Return the minimum number of intervals u need to remove to make the result array non overlapping..
Remember this, only take the interval that ends first, so wheen u compare current end and next start, if there
is an overlap, u increase the counter to count the interval u want to exclude inorder to make it non overlapping .
And in this process, u eliminate the interval that ends late... thus u take prevEnd = min(prevEnd, next_end)
"""
n = int(input('Enter the len of intervals '))
intervals = [[int(x) for x in input().split()] for y in range(n)]


def countMinOverlappingIntervals():
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]
    prevStart = intervals[0][0]

    for next_start, next_end in intervals[1:]:

        if prevEnd <= next_start:
            prevEnd = next_end
            prevStart = next_start

        else:
            res += 1
            prevEnd = min(prevEnd, next_end)

    return res

print(countMinOverlappingIntervals())