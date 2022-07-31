

arr = [int(x) for x in input().split()]

def calPollution():

    totalPolution = 0
    for i in arr:
        totalPolution += i

    arr.sort(reverse=True)

    goal = 0
    curr = arr[0]
    next = arr[1]
    while True:
        if goal >= totalPolution / 2:
            break

        while curr > next:
            curr = curr / 2





    pass


1000 -- 100

500
250
125
64.5

10



