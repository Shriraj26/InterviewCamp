"""
Eg - 1,2,3,4,5 =>  5,4,3,2,1
Just have 2 start and end pointers at start index 0 and at len(arr) - 1 then do start++ and do end--
until u have start < end, u can swap starting and ending indices...
"""

arr = [int(x) for x in input().split()]

start = 0
end = len(arr)-1
while start < end:

    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)