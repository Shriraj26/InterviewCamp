"""
Search Array of Unknown lengthYou are given an array, but you don't know the length.
Write a program to finds target element in the array.

This is a very good question and u need to follow some steps inorder to get the result!!!
1. Find where we get exception... In this step, we increment i by multiplying it by 2 all the way and accessing the
    element at arr[i]... thus i goes from 0 2 4 8 16 32 .... and so on multiplies
2. After we get the index where got the exception, now we know that the length of the array should be between
    exception/2 and exception   as i gets multiplied by 2 the length should be there
    in between... So now we apply binary search and then try to access the mid elem
        1. If we can access mid check for mid+1, if mid+1 gives exception, this means that we have now reached the length of the array
        2. If we cannot access mid, it means that we need to go back, do end = mid-1
        3. If we are able to access mid and also mid+1 this means that we need to go further, then we do start = mid+1
3. After we finally get the last index of the array itself, the last thing is left to search for the target elem, apply simple
    binary search and then u will get the result!!!

"""

arr = [int(x) for x in input().split()]
target = int(input())


# To get the index where we get the exception
def findException():
    i = 0
    try:
        while True:
            temp = arr[i]
            if i == 0:
                i = 2
            else:
                i = i * 2
    except:
        return i


endpointException = findException()


# To get the index of the last element of the array
def findArrayLength():
    start = endpointException // 2
    end = endpointException

    while start <= end:

        # find mid
        mid = start + (end - start) // 2

        # Try to access the mid
        try:
            temp = arr[mid]
        # if not able to access this means that u have travelled further, go back
        except:
            end = mid - 1
            continue

        # If u can access mid then check if u can access mid+1, if not then mid is your last elem in array
        # else u need to go further
        try:
            temp = arr[mid + 1]
        except:
            print('Found the end !!')
            return mid

        start = mid + 1


lastIndex = findArrayLength()

print('The last index of array is - ', lastIndex)
print('Length of array is - ', lastIndex + 1)


# Finally, apply the binary search on the array
def binSearch():
    start = 0
    end = lastIndex

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid

    return -1


print('Your element is at index - ', binSearch())
