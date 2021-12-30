"""
Now we will use memoization to store our result!! This improves runtime of Recursive functions
Time Complexity: O(n)
Space Complexity: O(n)
In this we have used array as a dp table but u can use a dictionary too
"""
x = int(input('Enter the number whose fibonacci u want to calculate with Memoization - '))
dp = [None for i in range(x + 1)]
dp[0] = 0
dp[1] = 1


def fibonacciMemoization(n):
    # base case if n == 0 or n == 1
    if n == 1 or n == 0:
        return dp[n]

    # First check if we have stored the result or not
    if dp[n] is None:
        ans1 = fibonacciMemoization(n - 1)
        ans2 = fibonacciMemoization(n - 2)
        dp[n] = ans1 + ans2

    return dp[n]


print(fibonacciMemoization(x))
