"""
Calculate nth term of fibonacci
Time Complexity: O(2^n)
Space Complexity: O(n)
"""


def fibonacci(n):

    # base case
    if n == 0 or n == 1:
        return n

    # recursive case
    ans1 = fibonacci(n-1)
    ans2 = fibonacci(n-2)

    # Finally return the answer
    return ans1 + ans2

x = int(input('Enter the number whose fibonacci u want to calculate '))
print(fibonacci(x))