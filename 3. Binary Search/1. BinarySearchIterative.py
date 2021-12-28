"""
Here we will be using an iterative version for the binary search... Instead of the recursive version, it is recommended
to use this version
Instead of using  mid = (start + end)/2  to calculate the midpoint,we use mid = start + (end - start)/2.
This has become a popular question.Why do we use this? Let's say start and end were very large integers.
We know they cannot be larger than 2^31 - 1 (~2billion), because they are given to us as integers
(assuming integer size of 32 bytes).However, their sum could be larger. This is called an integer overflow.In an integer
overflow, start + end would wrap around the max value into the negatives. If it is an unsigned integer, the value would wrap around 0.
"""

# Enter the sorted array as binary search works only on sorted arrays!!
arr = [int(x) for x in input().split()]
target = int(input())


def binSearch():
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid

    return -1


print(binSearch())
