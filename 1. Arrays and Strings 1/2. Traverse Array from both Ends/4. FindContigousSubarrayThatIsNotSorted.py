"""Given an array of integers, find the continuous subarray, which when sorted, results in the entire array being
sorted. For example: A = [0,2,3,1,8,6,9], result is the subarray [2,3,1,8,6]
0. Find min and max nums
1. Find the first dip
2. Find the first rise
3. Expand Left till u get the number that is smaller than the minValue to include all the greater numbers
4. Expand right if u get a number that is greater than the maxValue to include all the smaller numbers
"""
import sys

arr = [int(x) for x in input().split()]


# This returns the starting till it finds first dip encountered
def findStart():
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return i


# This returns the Ending index till it finds first increase in the value from end
def findEnd():
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i


def findMinMax(subArr):
    minNum = sys.maxsize
    maxNum = -sys.maxsize
    for i in subArr:
        minNum = min(minNum, i)
        maxNum = max(maxNum, i)

    return minNum, maxNum


def expandSubArray(start, end, minNum, maxNum):
    newArr = []
    newStart = 0
    newEnd = 0

    # expand Left till u get the number that is smaller than the min Value to include all the greater numbers
    i = start
    while i >= 0:
        if arr[i] < minNum:
            #print('Hey ',arr[i], minNum)
            newStart = i + 1
            break
        i -= 1

    # expand right if u get a number that is greater than the min Value to include all the smaller numbers
    i = end
    while i < len(arr):
        if arr[i] > maxNum:
            newEnd = i - 1
            break
        i += 1

    # return the indices of the subarrays!
    return newStart, newEnd


start = findStart()
end = findEnd()
minNum, maxNum = findMinMax(arr[start:end + 1])
subArr = expandSubArray(start, end, minNum, maxNum)
subArrStart, subArrEnd = expandSubArray(start, end, minNum, maxNum)
# print(start, end)
# print(minNum, maxNum)
# print(subArrStart, subArrEnd)
print('The shortest subarray that needs to be sorted to make the array completely sorted is - ')
print(arr[subArrStart:subArrEnd + 1])
