"""
Keep - the interval that ends first
Count where there is conflict


"""
n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]

def nonOverlapCount():

    # sort the array
    arr.sort( key = lambda i : i[0])

    prev_start = arr[0][0]
    prev_end = arr[0][1]
    count = 0

    for i in range(1, len(arr)):
        interval = arr[i]

        # if there is merging
        if prev_end > interval[0]:
            prev_end = min(prev_end, interval[1])
            count += 1

        else:
            prev_end = interval[1]

    print(count)



nonOverlapCount()