arr = [int(x) for x in input().split()]

minTilli = float('inf')
maxTilli = -float('inf')
maxTradeEver = 0
bestTradeTilli = [None] * len(arr)
bestTradeFromi = [None] * len(arr)

for i in range(len(arr)):
    minTilli = min(minTilli, arr[i])
    maxTradeEver = max(maxTradeEver, arr[i] - minTilli)
    bestTradeTilli[i] = maxTradeEver

maxTradeEver = 0
for i in range(len(arr)-1, -1, -1):
    maxTilli = max(maxTilli, arr[i])
    maxTradeEver = max(maxTradeEver, maxTilli - arr[i])
    bestTradeFromi[i] = maxTradeEver

maxTradeEver = 0
# calculate final max Trade -
for i in range(len(bestTradeTilli)):
    maxTradeEver = max(maxTradeEver, bestTradeTilli[i] + bestTradeFromi[i])

print(maxTradeEver)