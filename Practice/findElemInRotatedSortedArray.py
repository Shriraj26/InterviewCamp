
arr= [int(x) for x in input().split()]
elem = int(input('Enter the elem to search '))

def findelem():

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] == elem:
            return mid

        # array is sorted from start to mid
        if arr[mid] >= arr[start]:

            if elem >= arr[start] and elem < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # array is not sorted from start to mid
        else:
            if elem > arr[mid] and elem <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

print('Find this elem - ',findelem())