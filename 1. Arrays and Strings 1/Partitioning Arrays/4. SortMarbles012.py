"""
Given an array with n marbles colored Red, White or Blue, sort them so that marbles of the same color are adjacent, with the colors in the order Red, White and Blue.
Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).
For example, if A = [1,0,1,2,1,0,1,2], Output = [0,0,1,1,1,1,2,2].
We will be using the Dutch National Flag Approach to solve this problem!!! this is similar to the one where we have
the pivot as 1
"""

arr = [int(x) for x in input().split()]

i = 0
lessThanPivot = 0
greaterThanPivot = len(arr)-1
pivot = 1

while i <= greaterThanPivot:

    if arr[i] < pivot:
        arr[i], arr[lessThanPivot] = arr[lessThanPivot], arr[i]
        lessThanPivot += 1
        i += 1

    elif arr[i] > pivot:
        arr[i], arr[greaterThanPivot] = arr[greaterThanPivot], arr[i]
        greaterThanPivot -= 1

    else:
        i += 1

print(arr)