"""
A = [1,2,4,5,6,8] and T = 3, return index 2
A = [1,2,4,5,6,8] and T = 0, return index 0
A = [1,2,4,5,6,8] and T = 4, return index 3.
"""
arr = [1, 2, 4, 5, 6, 8]
target = 3


def modBinSearch(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            if mid == 0 or arr[mid-1] <= target:
                return mid
            else:
                end = mid - 1

        else:
            if mid == len(arr)-1 or arr[mid + 1] >= target:
                return mid + 1
            else:
                start = mid + 1


print(modBinSearch([1, 2, 4, 5, 6, 8], 9))
print(modBinSearch([1, 2, 4, 5, 6, 8], 0))
print(modBinSearch([1, 2, 4, 5, 6, 8], 3))
print(modBinSearch([1, 2, 4, 5, 6, 8], 7))
