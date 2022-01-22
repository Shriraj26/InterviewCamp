"""
For the previous question, how much money can you make with 2 trades...

Now, we will first calulate the regular best trade TILL ith position
We now will calculate best trade FROM ith position, for this purpose, we will traverse the array in reverse, and
then observe a drop!! this is same as calculating the best trade till i but in reverse!!!
After we have both, then we can get 2 things at ith position -
.....best_till_i
                i
                best_from_i....
Then just add these two to get the 2 trades!!! best_till_i + best_from_i ...and save max to record max yet..
Then u get an answer
"""

arr = [int(x) for x in input().split()]

best_trade_till_i = [None]*len(arr)
best_trade_from_i = [None]*len(arr)


def getBestTradeTilli():
    min_till_i = float('inf')
    max_trade_ever = 0
    for i in range(len(arr)):

        min_till_i = min(min_till_i, arr[i])

        max_trade_ever = max(max_trade_ever, arr[i] - min_till_i)

        best_trade_till_i[i] = max_trade_ever


def getBestTradeFromi():

    max_till_i = -float('inf')
    max_trade_ever = 0
    for i in range(len(arr)-1, -1, -1):

        max_till_i = max(max_till_i, arr[i])
        max_trade_ever = max( max_trade_ever, max_till_i - arr[i])

        best_trade_from_i[i] = max_trade_ever


def getMaxFrom2Trades():
    print(best_trade_till_i)
    print(best_trade_from_i)
    maxOf2Trades = -float('inf')
    for i in range(len(arr)):
        maxOf2Trades = max(maxOf2Trades, best_trade_till_i[i] + best_trade_from_i[i])
    return maxOf2Trades

getBestTradeTilli()
getBestTradeFromi()
print(getMaxFrom2Trades())