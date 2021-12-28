"""
Given a sorted array give indices of 2 numbers in the array that sum up to an target K...
start will be 0 and end will be len(arr) - 1, check at any point arr[start] + arr[end] == K, if yes
then return those indices start and end...
Ques to ask interviewer are that the array should be sorted in order to get the Target
"""


def twoSum():
    start = 0
    end = len(arr) - 1
    while start < end:
        currentSum = arr[start] + arr[end]
        if currentSum == K:
            return [start, end]
        elif currentSum > K:
            end -= 1
        else:
            start += 1

    return [None, None]

#Give the input in sorted manner!!!
arr = [int(x) for x in input().split()]
K = int(input())
print(twoSum())


