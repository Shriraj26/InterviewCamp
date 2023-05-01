"""
Given an array of integers, find the contiguous subarray (with at least 1 element) with the maximum sum.
The array can contain both negative and positive integers.
Ex -
-2, -3, 4, -1, -2, 1, 5, -1 => The max Sum of a subArray is - 7 that we get from 4,-1,-2,1,5

Max sum at a[i] is either - only a[i] or prev_sum(till a[i-1])+a[i]

Kadane's Algorithm uses Dynamic Programming, This is the condition that we need to check -
maxSumAt i = max( a[i]+maxSumAt i-1 ,  a[i]  )
Therefore, we either include the sum at i-1 + a[i] or we only take a[i]
We also take a global variable to store our maxSum possible till now..
Here instead of using a DP table that takes O(N) space, we will use a single variable to store the maxSum till now
that is ar i-1 variable and thus our solution will be taking O(1) space...
Now, to get the indices of the subArray, the maxSum will update twice - once when there is an increase in the maxSumTillNow,
then again when we reach the end... as the sumArray will have max Sum at the last index, we will monitor the increase twice
using the count, for first increase we will assign that index to start and next increase to the end... then we will return tne
subArray that has the max Sum...
"""


arr = [int(x) for x in input().split()]

maxSum = arr[0]
maxSumTillNow = arr[0]
start = 0
end = 0

for i in range(1, len(arr)):

    # At i, will will check arr[i] + maxSum till now and store the max too
    maxSumTillNow = max( maxSumTillNow + arr[i], arr[i])

    # to check if max summ till i is arr[i] this means that subarray has started that will give max sum
    if maxSumTillNow == arr[i]:
        start = i

    maxSum = max(maxSum, maxSumTillNow)
    # To check if the maxSum has now reached the end, then end will be assigned accordingly
    if maxSum == maxSumTillNow:
        end = i

    
    # maxSum = max( maxSumTillNow, maxSum)

print('MaxSum is - ',maxSum)
print('SubArray containing the maxSum is - ',arr[start: end+1])