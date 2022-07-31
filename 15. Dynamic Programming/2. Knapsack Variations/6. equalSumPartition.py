"""
in how many ways can u split an array into 2 parts such that their sum is equal!
Now, just apply subset sum where sum = array Sum / 2
"""
print('Enter the array ')
arr = [int(x) for x in input().split()]
K = int(input('enter the value of K '))
arrSum = 0
for i in range(len(arr)):
    arrSum += arr[i]

if arrSum % 2 == 1:
    print('Cannot split')
else:
    arrSum = arrSum // 2


K = arrSum
t = [[-1 for i in range(K + 1)] for j in range(len(arr) + 1)]



# print(len(t), len(t[0]))
def isSubSetSum():
    # init the dp table
    for i in range(len(arr) + 1):
        for j in range(K + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1

    # Jabardast
    for i in range(1, len(arr) + 1):
        for j in range(1, K + 1):

            # include the elem if its value is less than current sum
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[len(arr)][K]


print(isSubSetSum())
