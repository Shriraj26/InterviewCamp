
arr = [int(x) for x in input().split()]
target = int(input())
def binSearch():
    start = 0
    end = len(arr) - 1

    while start <= end:
        
        mid = start + (end - start)//2
        
        if arr[mid] > target:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            else:
                end = mid - 1

        elif arr[mid] <= target:
            if mid == len(arr) - 1:
                return mid
            else:
                start = mid + 1        
    
    return -1

print("Elem found at - ",binSearch())