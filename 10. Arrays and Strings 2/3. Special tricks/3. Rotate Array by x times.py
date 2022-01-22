"""
Rotate an array by X times
Ex -
1 2 3 4 5 6
by 2 times -
6 5 1 2 3 4

Aoproach -
Just reverse an array , say - 6 5 4 3 2 1 and k = 3
Then reverse a portion of array from index 0 to k-1 --- 4 5 6 3 2 1
Then reverse a portion of array from index k to len(arr)-1  --- 4 5 6 1 2 3
Finally we have 6 5 1 2 3 4
"""

arr = [int(x) for x in input().split()]
k = int(input())

def rotateArr(nums, k):

    k = k % len(arr)
    print(k)

    if k == 0:
        return

    # reverse the array
    reverseArr(nums, 0, len(nums) - 1)

    # reverse the array till k-1
    reverseArr(nums, 0, k - 1)

    # reverse the array after k
    reverseArr(nums, k, len(nums) - 1)

    print(nums)

def reverseArr(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


rotateArr(arr, k)



