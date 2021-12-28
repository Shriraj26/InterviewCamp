"""
Given an Array in sorted order, return squares of that array also in sorted order
Ex - [-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]
First take square of entier array, then compare arr[start], arr[end] take max of those and put it into a different
array
"""

arr = [int(x) for x in input().split()]
for i in range(len(arr)):
    arr[i] *= arr[i]
#print(arr)

start = 0
end = len(arr) - 1
newArr = []
while start <= end:
    if arr[start] > arr[end]:
        newArr.append(arr[start])
        start += 1
    else:
        newArr.append(arr[end])
        end -= 1

#now just either print in the array in reverse or actually slice the array
print(newArr[::-1])