

def binSearch(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start)//2

        if arr[mid] == target:
            print('Found the elem')
            return mid

        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1

    print("did not find the elem ")
    return -1

def binSearchFirstOccur(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start)//2

        if arr[mid] == target:
            if mid > 0 and arr[mid - 1] == target:
                end = mid - 1
            else:
                print('Found the first occurrence')
                return mid

        elif arr[mid] > target:
            end = mid - 1
        
        else:
            
            start = mid + 1

    print("did not find the elem ")
    return -1

def binSearchIndexToInsert(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start)//2

        print('start, mid, end - ', arr[start], arr[mid], arr[end])
        
        if arr[mid] <= target:
            if mid == len(arr) - 1:
                return mid
            start = mid + 1

        else:
            if mid == 0 or arr[mid - 1] <= target:
                return mid
            end = mid - 1

def record(arr, mid, result, target):

    if result == None:
        result = mid
        return result
    
    if abs(arr[mid] - target) < abs(result - target):
        result = mid
    
    return result

def recordAndMoveOn(arr, target):
    
    start = 0
    end = len(arr) - 1
    result = None

    while start <= end:

        mid = start + (end - start) // 2

        result = record(arr, mid, result, target)

        if arr[mid] == target:
            return mid, result

        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
        
    
    return -1, result





            

    

print("Enter the elems of the array ")
arr = [int(x) for x in input().split()]
print("Enter the target elem ")
target = int(input())

index = binSearch(arr, target)
print('index - ', index)

firstOccur = binSearchFirstOccur(arr, target)
print('first occur at index - ', firstOccur)

indexToInsert = binSearchIndexToInsert(arr, target)
print('binSearchIndexToInsert occur at index - ', indexToInsert)

index, elemClosestToTarget = recordAndMoveOn(arr, target)
print("elemClodst t target ", elemClosestToTarget)