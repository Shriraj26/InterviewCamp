"""
Return the minimum number of meeting rooms required to host meetings, now,
U need to get the maximum overlap!!! For this, u mantain 2 arrays, start and end and their pointers too
Sort these 2 arrays
Then, if value at start is less then end, it means that meeting has been started, inc the count and inc start ptr
if value of start is equal to end or greater than, it means meeting has been ended and another meeting has been started,
for this, we first inc end ptr and then decrement the count
In this process, u can reach a max in count, so keep a track of the count as well...
Refer here - https://www.youtube.com/watch?v=FdzJmTCVyJU
"""
n = int(input('Enter the len of intervals '))
intervals = [[int(x) for x in input().split()] for y in range(n)]

def countMeetingRooms():
    count = 0
    if len(intervals) <= 1:
        return count + 1

    maxRooms = 0

    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    startPtr = 0
    endPtr = 0

    while startPtr < len(intervals):

        if start[startPtr] < end[endPtr]:
            count += 1
            startPtr += 1
        else:
            count -= 1
            endPtr += 1

        maxRooms = max(maxRooms, count)

    return maxRooms


print(countMeetingRooms())



