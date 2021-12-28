"""
Now, given an array, move all zeroes to the end of the array.
For example, [4,2,0,1,0,3,0] -> [4,1,2,3,0,0,0]
Note that here the order of the non-zero numbers is not that important...
This is same as the previous one...Now traverse from the end and check if u encounter a zero, if yes then swap with the
end of the array and then decrement the end pointer in our case it is the boundary
"""

arr = [int(x) for x in input().split()]

boundary = len(arr)-1
i = len(arr)-1
while i >= 0:

    if arr[i] == 0:
        arr[i], arr[boundary] = arr[boundary], arr[i]
        boundary -= 1
    i -= 1

print(arr)

