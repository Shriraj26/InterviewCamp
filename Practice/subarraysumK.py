"""
Prac Subarray sum
"""
arr = [int(x) for x in input().split()]
k = int(input())
dict = {}
totalSum = 0

for i in range(len(arr)):
    totalSum += arr[i]

    if totalSum == k:
        print(arr[0:i+1])
        break

    if dict.get(totalSum - k) is not None:
        print(arr[dict.get(totalSum) + 1: i + 1])
        break

    dict[totalSum] = i
