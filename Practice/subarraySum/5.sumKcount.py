arr = [1,1,2]
k = 2

myDict = {}
totalSum = 0
count = 0
for i in range(len(arr)):
    totalSum += arr[i]

    if totalSum == k:
        count += 1

    if myDict.get(totalSum - k) is not None:
        count += myDict[totalSum - k]

    myDict[totalSum] = myDict.get(totalSum, 0) + 1


print(count)