"""
fibo Memo that is with dp table - 1d
"""



n = int(input('Enter value of n for memo fibo '))
dp = [None] * (n+1)

#init the array
dp[0] = 0
dp[1] = 1

def topDown():
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(topDown())


