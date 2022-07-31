"""
You can do as many transactions as u want, return the max trade...
this is a very simple code, just observe rise in the price... if there is such a rise, then add it to the profit,
if not then return

"""
prices = [int(x) for x in input().split()]

profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

print(profit)

