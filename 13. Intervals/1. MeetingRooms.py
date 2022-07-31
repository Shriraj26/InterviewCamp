"""
Decide if a person can attend all the meetings in one hall
This is easy, just check if there is an overlap, if not then return True
"""

n = int(input('Enter the len of intervals '))
intervals = [[int(x) for x in input().split()] for y in range(n)]

def checkOverlap():
    if len(intervals) <= 1:
        return True

    intervals.sort(key=lambda i: i[0])

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if end > interval[0]:
            return False
        end = interval[1]

    return True


print(checkOverlap())