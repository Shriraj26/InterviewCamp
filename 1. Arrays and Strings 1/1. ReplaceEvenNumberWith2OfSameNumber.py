"""
Given an array of numbers, replace each even number with 2 of the same
Ex - [1,2,5,6,8] -> [1,2,2,5,6,6,8,8]
Approach -
As all the modifications need to be done on the same array itself, We will assume that the length
of input array is big enough to accomodate the numbers that we need to duplicate as well
We will traverse the array in reverse and have 2 pointers start and end
end will be at the end of the array and start will be at the array where last element is without the
extra spaces provided. say array is -  [1,2,5,6,8, -1, -1, -1]  we will consider -1 as the extra spaces
therefore end will be at - -1 that is the last in the array and start will be at where 8 is currently.

Therefore, if start is even, copy a[start] to a[end], decrease end, again copy a[start] to a[end] decrease end
If the start is odd then just copy a[start] to a[end] once and decrease end.
"""

#Give input as - [1,2,5,6,8,-1,-1,-1] where -1 elements are the one with extra spaces equaling to the number of
#even numbers in the array so in the example we have 3 even elements 2, 6, 8 then we have 3 trailing -1s


def returnStartIndex(arr):
    i = len(arr)-1
    while i >=0:
        if arr[i] != -1:
            return i
        i -= 1

arr = [int(x) for x in input().split()]

start = returnStartIndex(arr)
end = len(arr) - 1
while start >= 0:

    if arr[start] % 2 == 0:
        arr[end] = arr[start]
        end -= 1
        arr[end] = arr[start]
        end -= 1
    else:
        arr[end] = arr[start]
        end -= 1

    start -= 1
print(arr)

