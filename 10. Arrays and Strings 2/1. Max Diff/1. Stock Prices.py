"""
Given a list of stock prices for a company, find the maximum amount of money you could have made with one trade
(one buy/sell). For example, if A = [2,3,1,4,5,7,5,4], the max money with a single trade is 6, if you buy at 1 and sell at 7.

When u think of this question, always think in terms of graph, from where the stock starts and how will u proceed when u
want to calculte the mzx difference ever

Approach - In this question, u can calculate the max_trade at ith position...
For that u will need -
1. Min elem so far till ith position
2. a[i] .. that is the elem at a[i]

The algo is this -
1. Calculate the min so far till ith position by comparing the current and recorded min
2. then calculate max_trade_At ith position by subtracting a[i] - min_so_far
3. then have a variable to record the most maximum trade - max_yet = max( max_yet, max_at_i)
"""


arr = [int(x) for x in input().split()]

def calcuateMaxGain():
    min_till_i = float('inf')
    max_trade_ever = 0
    max_trade_at_i = 0
    for i in range(len(arr)):
        min_till_i = min(min_till_i, arr[i])
        max_trade_at_i = arr[i] - min_till_i
        print(max_trade_at_i, arr[i])
        max_trade_ever = max(max_trade_ever, max_trade_at_i)

    return max_trade_ever



print(calcuateMaxGain())







