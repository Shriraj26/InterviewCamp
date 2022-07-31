"""
fibo Memo that is with dp table - 1d
"""



n = int(input('Enter value of n for memo fibo '))
dp = [None] * (n+1)
dp[0] = 0
dp[1] = 1

def fiboMemo(n):

    if n == 0 or n == 1:
        return dp[n]

    if dp[n] is None:
        dp[n] = fiboMemo(n-1) + fiboMemo(n-2)

    return dp[n]



print(fiboMemo(n))
