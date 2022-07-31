arr = [int(x) for x in input().split()]

min_till_i = float('inf')
max_trade = -float('inf')

for i in range(len(arr)):
    min_till_i = min(min_till_i, arr[i])
    max_trade = max(max_trade, arr[i] - min_till_i)

print(max_trade)