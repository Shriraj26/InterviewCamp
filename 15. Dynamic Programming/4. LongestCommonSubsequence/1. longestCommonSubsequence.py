X = input('Enter String 1 ')
Y = input('Enter String 2 ')
n = len(X)
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

def lcsequence(n, m):

    if n == 0 or m == 0:
        return 0

    if t[n][m] != -1:
        return t[n][m]

    if X[n-1] == Y[m-1]:
        t[n][m] =  1 + lcsequence(n-1, m-1)
    else:
        t[n][m] =  max(lcsequence(n-1, m), lcsequence(n, m-1))

    return t[n][m]


print(lcsequence(n, m))


