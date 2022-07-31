arr = [2,4,-2,1,-3,5,-3]

myDict = {}

def sum0():
    totalSum = 0
    for i in range(len(arr)):

        totalSum += arr[i]

        if totalSum == 0:
            return arr[0: i+1]

        if myDict.get(totalSum) is not None:
            return arr[myDict.get(totalSum)+1 : i+1]

        myDict[totalSum] = i
        print(myDict)

print(sum0())