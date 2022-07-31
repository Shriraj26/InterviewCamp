arr = [2,4,-2,1,-3,5,-3]
k = 5

def subArraySumK():

    totalSum = 0
    myDict = {}
    for i in range(len(arr)):

        totalSum += arr[i]

        if totalSum == k:
            i1 = 0
            i2 = i
            return arr[i1: i2+1]

        elif myDict.get(totalSum - k) is not None:
            i1 = myDict.get(totalSum - k) + 1
            i2 = i
            return arr[i1: i2+1]

        myDict[totalSum] = i

print(subArraySumK())

