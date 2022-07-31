"""
Given a sorted array of Integers, find the target. If the target is not found,return the element closest to the target.
For example,A = [1,2,4,5,7,8,9], Target = 6 -> Output Index = 3 or 4 (since both 5 and 7 are equally close)

In this we will be using a record and move on technique... We will initially set a result that is null
Then we will be storing the elements that are closer to the target by getting the difference between
target and the arr[mid] and also target and arr[result] ... result is the index of the element that is closest
to the target...
Everything is same as binary search, but we have just added a function that will check and update the result or
the element closest to the target
"""

arr = [int(x) for x in input().split()]
target = int(input())


def record(mid, result):
    # First time when we check if result is None or infinity, we will assign it to a value say mid as a closer one
    if result is None:
        result = mid

    # find out the difference between arr[mid], target and arr[mid],arr[result]
    if abs(arr[mid] - target) < abs(arr[result] - target):
        result = mid

    return result


def binSearch():
    start = 0
    end = len(arr) - 1
    result = None
    while start <= end:
        mid = start + (end - start) // 2
        result = record(mid, result)
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return result


def recordTry(result, mid):

    if result is None:
        result = mid

    if abs(result - arr[mid]) < abs(target - arr[mid]):
        result = mid

    return result

def binSearch2():

    start = 0
    end = len(arr) - 1
    result = None
    while start <= end:

        mid = start + (end - start) // 2
        result = record(mid, result)
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return result

print(binSearch2())
