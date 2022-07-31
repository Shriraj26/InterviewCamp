print('Give input of positive and negative numbers ')
arr  = [int(x) for x in input().split()]
k = int(input())
myDict = {}

sum = 0
for i in range(len(arr)):

    sum += arr[i]

    if sum == k:
        print('Subarray till sum zero is - ',arr[:i+1])
        break

    if myDict.get(sum) is None:
        myDict[sum] = i
    elif myDict.get(sum-k):
        print('Subarray till sum zero is - ',arr[myDict[sum]+1: i+1])
        break



