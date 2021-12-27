"""
Given an array of integers A and a pivot, rearrange A in the following order:
[Elements less than pivot, elements equal to pivot, elements greater than pivot]

For example, if A = [5,2,4,4,6,4,4,3] and pivot = 4 -> result = [3,2,4,4,4,4,6,5]

Note: the order within each section doesn't matter.
This is a very good question and maybe asked though its easy...
have 2 boundaries for elem less than the pivot and elem greater than the pivot,
if elem less than the pivot, then swap with start boundary, increment start and i
ef elem greater than the pivot, then swap with the end boundary, but this time decrement end boundary, dont do anything with i,
if equal to pivot then only increment i
"""

arr = [int(x) for x in input().split()]
pivot = int(input())
#Two partitions for one less than a pivot, and one for more than a pivot
lessThan = 0
greaterThan = len(arr) - 1
i = 0

while i <= greaterThan:

    if arr[i] < pivot:
        arr[i], arr[lessThan]= arr[lessThan], arr[i]
        lessThan += 1
        i += 1
    elif arr[i] > pivot:
        arr[i], arr[greaterThan]= arr[greaterThan], arr[i]
        greaterThan -= 1
    else:
        i += 1

print(arr)