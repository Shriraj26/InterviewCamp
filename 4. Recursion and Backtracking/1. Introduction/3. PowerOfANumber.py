"""
Power Function: Implement a function to calculate x^n.
Both x and n can be positive/negative and overflow doesn't happen. Try doing it in O(log(n)) time.
We will not need Memoization here as we are not repeating any calls and we only use DP if we repeat any subproblems
"""

x = int(input('enter the number whose power u want to calculate - '))
n = int(input('enter the power of that number - '))


def power(x, n):

    # base case if the power is 0 or 1 then we return the numbers accordingly-
    if n == 0:
        return 1
    elif n == 1:
        return x

    ans = 0
    # recursive call
    if n%2 == 1:
        xHalf = power(x, (n-1)//2)
        ans = x * xHalf * xHalf

    else:
        xHalf = power(x, n//2)
        ans = xHalf * xHalf

    return ans


if n < 0:
    FinalAns = power(1/x, abs(n))
else:
    FinalAns = power(x, n)
print('Power of x is - ', FinalAns)