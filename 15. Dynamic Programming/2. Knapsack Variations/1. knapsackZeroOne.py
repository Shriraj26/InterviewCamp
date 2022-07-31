"""
We either include or exclude an element in 0 1 knapsack, to include it, subtract its weight,
and subtract the number by 1
To exclude it, dont do anything

"""

print('Enter weights and vals ')
W = [int(x) for x in input().split()]
val = [int(x) for x in input().split()]
n = len(val)
maxWeight = int(input())


def knspsack(n, maxWeight):
    # base case1 - of weight is zero or value is zero, return
    if n == 0 or maxWeight == 0:
        return 0

    if W[n - 1] <= maxWeight:
        include = val[n - 1] + knspsack(n - 1, maxWeight - W[n - 1])
        exclude = knspsack(n - 1, maxWeight)
        print(n - 1, include, exclude)
        return max(include, exclude)

    else:
        exclude = knspsack(n - 1, maxWeight)
        print('Exclude - ', exclude)
        return exclude


def knapSackMemo(n, maxWeight):
    if n == 0 or maxWeight == 0:
        return 0

    if dp[n][maxWeight] != -1:
        return dp[n][maxWeight]

    else:
        if W[n - 1] <= maxWeight:
            dp[n][maxWeight] = max(val[n - 1] + knapSackMemo(n - 1, maxWeight - W[n - 1]),
                                   knapSackMemo(n - 1, maxWeight))
        else:
            dp[n][maxWeight] = knapSackMemo(n - 1, maxWeight)

    return dp[n][maxWeight]

def knapSackTopDown():

    # initialize the array
    for i in range(n+1):
        for j in range(maxWeight + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1,n+1):
        for j in range(1,maxWeight + 1):

            if W[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j - W[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[n][maxWeight]


dp = [[-1 for i in range(maxWeight + 1)] for j in range(n + 1)]
t = [[-1 for i in range(maxWeight + 1)] for j in range(n + 1)]

print(knapSackTopDown())
print(dp)
