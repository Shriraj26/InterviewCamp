"""
Given a sorted array that can contain duplicates, find the first occurrence of the target element.
For example:A = [1,3,4,6,6,6,7] and Target = 6, return index 3.

There is just one small modification to be made in this problem,
As u need to find the first occurrence, then u need to go left again or mid-1 again.,,
U can go mid-1 on 2 conditions -
1. arr[mid] > target
2. if u get the element but some things need to be satisfied as well -
    1. arr[mid] == target and mid > 0 and arr[mid-1] == target  ... then do mid-1
"""

# Enter the sorted array with some duplicates to check if our code works or not
arr = [int(x) for x in input().split()]
target = int(input())


def binSearch():
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2
        # print(start, end, mid)

        if arr[mid] < target:
            start = mid + 1

        elif (arr[mid] > target) or ((arr[mid] == target) and (mid > 0) and arr[mid-1] == target):
            end = mid - 1

        else:
            return mid

    return -1


print(binSearch())
