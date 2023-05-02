"""
In this, the arr[start] <= arr[mid].. the = sign is most imp!!

Check the first elem and mid of the subarrays!!
This is diff from the find min in rotated sorted in the sense that in rotatad
arr when we find min, we compare mid with a[0], but here we do it with arr[start]!!
1. If arr[mid] == elem, return it!!

2. if arr[start] <= arr[mid], then  ... <= sign is imp and < should not be there!!!
        Check if arr[start] <= target < arr[mid]:
            if yes then go left
            else go right
3. else (arr[start] > arr[mid]):    
        Check if arr[mid] < target <= arr[end]:
            if yes, then go right,
            else go left

"""


class Solution:
    def search(self, arr: List[int], elem: int) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:

            mid = start + (end - start) // 2
            if arr[mid] == elem:
                return mid

            if arr[start] <= arr[mid]:
                if arr[start] <= elem < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if arr[mid] < elem <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
