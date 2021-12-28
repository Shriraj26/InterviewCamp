"""
You are given a sorted array A and a target T. Return the index where T would be placed if inserted in order. For example,

A = [1,2,4,5,6,8] and T = 3, return index 2
A = [1,2,4,5,6,8] and T = 0, return index 0
A = [1,2,4,5,6,8] and T = 4, return index 3.

This question can also be formulated as - Find the first element that is larger than the target!!!
Decision to go here and there can be done as -
1. if arr[mid] is smaller or equal to target - we need to go right that is do mid+1
    - but before doing that check if its the last element of the arrau, if yes then return as it as
    - else go right
2. if arr[mid] is greater than the target, - we need to go left!!!
    - but before that check if it is not the first element or also check the V.V.V.imp condition -
        if arr[mid-1] is less than the mid... this means that now we can insert our element!!!

Go through the code once,you will get the idea how it works!! This is the exact same code that I wrote and
is in the InterviewCamp as well
"""

# Enter the sorted array as binary search works only on sorted arrays!!
arr = [int(x) for x in input().split()]
target = int(input())


def binSearch():
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] <= target:
            if mid == len(arr)-1:
                print('mid1 is - ',mid)
                return mid
            start = mid + 1

        elif arr[mid] > target:
            if mid == 0 or arr[mid-1] <= target:
                print('mid2 is - ', mid)
                return mid

            end = mid - 1

    return -1


print(binSearch())
