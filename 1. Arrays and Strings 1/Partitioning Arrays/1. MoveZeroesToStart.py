"""
You are given an array of integers. Rearrange the array so that all zeroes are at the beginning of the array.
For example, [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]
Note that here the order of the non-zero numbers is not that important...
We traverse the array and swap the non-zero numbers with the zeroes that we come accross and increment the pointer
"""

arr = [int(x) for x in input().split()]

boundary = 0
i = 0
while i < len(arr):

    if arr[i] == 0:
        arr[i], arr[boundary] = arr[boundary], arr[i]
        boundary += 1
    i += 1

print(arr)

