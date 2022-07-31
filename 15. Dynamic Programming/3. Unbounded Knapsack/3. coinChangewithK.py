print('Enter the array of coins ')
arr = [int(x) for x in input().split()]
total = int(input('Enter the total value - '))
K = int(input('Enter the value of k - '))

t = [[[-1 for k in range(K + 1)] for j in range(total + 1)] for i in range(len(arr) + 1)]


def coinChangeMemo(n, Total, K):
    print(n, Total, K)
    if n == 0:
        if Total == 0:
            if K == 0:
                return True
            else:
                return False
        else:
            return False

    if t[n][Total][K] != -1:
        # print('Here ',n,Total, K)
        return t[n][Total][K]

    if arr[n - 1] <= Total:
        without = coinChangeMemo(n - 1, Total, K)
        if K > 0:
            t[n][Total][K] = coinChangeMemo(n, Total - arr[n - 1], K - 1) or without
        else:
            t[n][Total][K] = without
    else:
        t[n][Total][K] = coinChangeMemo(n - 1, Total, K)

    return t[n][Total][K]


print('Decision - ', coinChangeMemo(len(arr), total, K))
print(t)
