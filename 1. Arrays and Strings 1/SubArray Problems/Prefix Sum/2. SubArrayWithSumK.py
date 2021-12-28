"""
Given an array of positive and negative integers, find a subarray whose sum equals X.
For example: Input = [2,4,-2,1,-3,5,-3], X = 5 --> Result = [2,4,-2,1]

This is very similar to the previous question, just instead of zero we will use the target here... and we
will check if the totalSum - target has been appeared before? if yes then return that index!!
"""

arr = [int(x) for x in input().split()]
target = int(input('Enter the target '))
indices = [None, None]

#A dictionary to store the summ till now and index too
totalDict = {}
totalSum = 0

for i in range(len(arr)):

    #calculate the totalSum
    totalSum += arr[i]

    #if the totalSum is 0 then return 0 to index
    if totalSum == target:
        indices[0] = 0
        indices[1] = i
        break

    #if u get the sum again this means that the sum might have been 0 in between so store the indeces here
    if totalDict.get(totalSum - target) is not None:
        indices[0] = totalDict.get(totalSum) + 1
        indices[1] = i
        break

    #else store the sum in the dictionary
    totalDict[totalSum] = i


print(totalDict)
print(indices)

