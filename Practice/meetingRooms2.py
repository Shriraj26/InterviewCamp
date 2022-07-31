"""
Return the minimum number of meeting rooms requirerd. For this we measure where the maximum conflict was at any point of time.

"""

n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]


def nonOverlap():

    # get start and end arrays
    start = sorted([i[0] for i in arr])
    end = sorted([i[1] for i in arr])

    start_ptr = 0
    end_ptr = 0
    count = 0
    maxConflict = 0
    while start_ptr < n:

        if start[start_ptr] < end[end_ptr]:
            count += 1
            start_ptr += 1
        else:
            count -= 1
            end_ptr += 1
        maxConflict = max(count, maxConflict)

    print(maxConflict)


nonOverlap()

