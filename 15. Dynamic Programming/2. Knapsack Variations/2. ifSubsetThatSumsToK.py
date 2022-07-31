"""
Return True if there exists a subset that sums to K
"""
print('Enter the array ')
arr = [int(x) for x in input().split()]
K = int(input('enter the value of K '))

t = [[-1 for i in range(K + 1)] for j in range(len(arr) + 1)]


# print(len(t), len(t[0]))
def isSubSetSum():
    # init the dp table
    for i in range(len(arr) + 1):
        for j in range(K + 1):
            if i == 0:
                if j == 0:
                    t[i][j] = True
                else:
                    t[i][j] = False
            if j == 0:
                t[i][j] = True

    # Jabardast
    for i in range(1, len(arr) + 1):
        for j in range(1, K + 1):

            # include the elem if its value is less than current sum
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[len(arr)][K]


print(isSubSetSum())
