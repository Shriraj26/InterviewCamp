import collections, math, bisect



def countTheQues(arr):
    if len(arr) <= 2:
        return []

    minElem = float('inf')
    maxElem = - float('inf')
    for i in range(len(arr)):
        minElem = min( minElem, arr[i])
        maxElem = max(maxElem, arr[i])

    print(minElem, maxElem)
    count = 0
    for i in range(len(arr)):

        if minElem < arr[i] < maxElem:
            count += 1


    print(count)

def nearestCity(points, xCoordinates, yCoordinates, queriedPoints): # binary search O(N*logN) of number of points
    XY, sameXY = {}, [collections.defaultdict(dict), collections.defaultdict(dict)]
    for p, x, y in zip(points, xCoordinates, yCoordinates):
        XY[p] = (x, y), (y, x)
        for (x, y), same in zip(XY[p], sameXY):
            same[x][y] = p
    sortXY = [{x: sorted(y) for x, y in same.items()} for same in sameXY]

    Near = collections.namedtuple("Near", ["distance", "point"])
    none, res = Near(math.inf, ""), []
    for p in queriedPoints:
        near = none
        for (x, y), same, sort in zip(XY[p], sameXY, sortXY):
            i = bisect.bisect_left(sort[x], y)
            near = min(
                near,
                Near(y - sort[x][i - 1], same[x][sort[x][i - 1]]) if i else none,
                Near(sort[x][i + 1] - y, same[x][sort[x][i + 1]]) if i < len(sort[x]) - 1 else none,
            )

        toAppend = near.point
        if toAppend == '':
            toAppend = None
        res.append(toAppend)
    return res

# countTheQues(arr)

c = input().split()
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
q = input().split()

print(nearestCity(c, x, y, q))

