"""
Given an array of positive integers, find the contiguous subarray that sums to a given number X.
For example, input = [1,2,3,5,2] and X=8, Result = [3,5]
Positive Numbers in the Array only!!

In this case, we have to find the subArray that sums to a target, given all the elements in the array are positive...
We will use a sliding window technique, we have a window and it has a start and end indices...
If we increase the end index it means that the window size will expand and as we have all the positive numbers, the sum will increase
if we increase the start index, it means that the window size will decrease and as we have all the positive numbers,
the sum will decrease...
Therefore end++ => sum increase ... start++ => sum decrease... thats it.. this is the core concept to remember...

Edge case to consider -
1. when will be stop --> when start index is greater than the last index of array  start < len(arr)
2. What happens if start and end indices appear at same point and then the start increases but end doesnt -
    Ex -
    5 3 1 7 6 24 2 3 --> consider start and end the index - 5 that it as element 24, and consider our target less than 24
    Now as sum is 24 and target is less than the sum, then we increase sum, but as start goes > end, we assign end to
    where start is that is, start and end will now both point to 2 that is at index 6 and then sum will become arr[start] == arr[end]
3. What if there is no such subArray that sums up to target - then return None, None
4. What if end index reaches the end of the array, then we have to break
"""

arr = [int(x) for x in input().split()]
target = int(input())

start = 0
end = 0
subArrSum = arr[0]
finalIndices = [None, None]

while start < len(arr):

    #Edge case to check if start does not go beyond the end index
    if start > end:
        end = start
        subArrSum = arr[start]

    if subArrSum < target:

        #edge case to check if end index does not go beyond the length of array
        if end == len(arr)-1:
            break
        end += 1
        subArrSum += arr[end]

    elif subArrSum > target:
        subArrSum -= arr[start]
        start += 1

    #when we finally get our solution!!! we save the indices in a temp array
    else:
        finalIndices[0] = start
        finalIndices[1] = end
        break

print(finalIndices)