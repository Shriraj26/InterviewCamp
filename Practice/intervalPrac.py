n = int(input())
arr = [[int(x) for x in input().split()] for j in range(n)]
finalArr = []

def merge():

    # sort
    arr.sort(key = lambda i: i[0])

    start = arr[0][0]
    end = arr[0][1]

    for i in range(1, len(arr)):

        interval = arr[i]

        # merge condition . end >= interval[0]
        if end >= interval[0]:
            end = max(end, interval[1])

        else:
            finalArr.append([start, end])
            start= interval[0]
            end = interval[1]

    finalArr.append([start, end])
    print(finalArr)
merge()
