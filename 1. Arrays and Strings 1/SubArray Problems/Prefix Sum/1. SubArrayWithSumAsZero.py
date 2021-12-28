"""
Given an array of integers, both -ve and +ve, find a contiguous subarray that sums to 0.
For example: [2,4,-2,1,-3,5,-3] --> [4,-2,1,-3]

Prefix sum is the cummulative sum used to calculate sum upto ith index...
Say array is - 1,2,3,4,5
Then prefix sum till index 3 or till elem 4 is - 1+2+3+4 = 10
Now the concept is this -
1. The array can have -ve numbers too
2. You can get sum of a subarray as 0 when -
    1. Either the sum from index 0 till any elem is 0 that is the prefix sum till that index
    2. if u get a sum that repeats again, it means that the sum might have been 0 in between and then it repeats again!!!
    Thus that is the index that u need to check for
"""

arr = [int(x) for x in input().split()]
indices = [None, None]

#A dictionary to store the summ till now and index too
totalDict = {}
totalSum = 0

for i in range(len(arr)):

    #calculate the totalSum
    totalSum += arr[i]

    #if the totalSum is 0 then return 0 to index
    if totalSum == 0:
        indices[0] = 0
        indices[1] = i
        break

    #if u get the sum again this means that the sum might have been 0 in between so store the indeces here
    if totalDict.get(totalSum) is not None:
        indices[0] = totalDict.get(totalSum) + 1
        indices[1] = i
        break

    #else store the sum in the dictionary
    totalDict[totalSum] = i


print(totalDict)
print(indices)

