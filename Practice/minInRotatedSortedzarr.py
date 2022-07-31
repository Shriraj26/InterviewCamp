"""
If the array is not rotated, then the last element is greater than the first element!!!
What an observation!!
Therefore
1. if last elem > first elem -- array not rotated, return the first elem
2. if last elem < first elem -- then the array is rotated, we need to think of our modified binary search!

Modified binary search - we need to find the inflection point where the list starts to increase in the
ascending order!
1. if mid < first elem -- the inflecion point is to left
2. if mid > first elem -- the inflection point is to the right
3. stop when one of these 2 conditions meet -
    1. if arr[mid] > arr[mid+1] -- means mid + 1 is smallest
    2. if arr[mid - 1] > arr[mid] -- means the mid is smallest
"""

arr = [int(x) for x in input().split()]


def findMin():
    start = 0
    end = len(arr) - 1

    # array is not rotated
    if arr[end] > arr[start]:
        return arr[0]

    # array is rotated
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        if arr[mid - 1] > arr[mid]:
            return arr[mid]
        print(arr[start], arr[mid], arr[end])

        # go right
        if arr[mid] < arr[0]:
            end = mid - 1
        else:
            start = mid + 1


print(findMin())
