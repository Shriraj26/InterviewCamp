"""
In this version of Knapsack, u are free to include as many items as u want!!
"""

print('Enter weights and vals ')
wt = [int(x) for x in input().split()]
val = [int(x) for x in input().split()]
n = len(val)
W = int(input('Enter max Weight '))

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def unboundedKnapsack():

    # init
    for i in range(n+1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    # play
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]


    return t[n][W]

print(unboundedKnapsack())