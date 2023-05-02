"""
Given a sorted array A that has been rotated in a cycle, find the smallest element of the array in O(log(n)) time. For example,

[1,2,4,5,7,8] rotated by 3 gives us A = [5,7,8,1,2,4] and the smallest number is 1.
[1,2,4,5,7,8] rotated by 1 gives us A = [8,1,2,4,5,7] and the smallest number is 1.

This is a unique one! in this we are using right most element as our pivot...
Every time the lowest number will be less than or equal to pivot,
and if that lowest number may -
1. Appear at index 0
2. or we can check the dip - arr[mid-1] > arr[mid]
If these conditions are satisfied then we are khush...
this u need to see once again!!! please revisit this problem...
"""

arr = [int(x) for x in input().split()]


def binSearchSmallestElement():
    start = 0
    end = len(arr) - 1
    right = arr[end]
    while start <= end:

        mid = start + (end - start) // 2

        # This is our master condition...
        if arr[mid] <= right:
            if mid == 0 or arr[mid - 1] > arr[mid]:
                return mid
            else:
                end = mid - 1

        elif arr[mid] > right:
            start = mid + 1

    return -1


print(binSearchSmallestElement())
