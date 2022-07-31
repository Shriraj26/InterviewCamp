"""
Just find inflection point,
1. Base case if array is not rotated, last elem will be greater than first elem
2. if arr[mid - 1] > arr[mid] --- arr[mid] will be the smallest
3. if arr[mid] > arr[mid+1] --- arr[mid+1] will be the smallest
4. if arr[mid] > arr[0] -- go right as right will have small elems
5. else go left
"""


arr = [int(x) for x in input().split()]

def search():

    # Case when array is already sorted
    if arr[-1] > arr[0]:
        return arr[0]

    start = 0
    end = len(arr)-1

    while start < end:
        mid = (start + end) // 2

        if arr[mid - 1] > arr[mid]:
            return arr[mid]
        elif arr[mid] > arr[mid+1]:
            return arr[mid + 1]

        if arr[mid] > arr[0]:
            # go right
            start = mid + 1
        else:
            # go left
            end = mid - 1

print(search())



