"""

"""
arr = [int(x) for x in input().split()]
target = int(input())

start = 0
end = len(arr) - 1

while start <= end:

    currSum = arr[start] + arr[end]
    print(arr[start], arr[end])
    if currSum == target:
        print(start, end)
        break
    elif currSum < target:
        start += 1
    else:
        end -= 1


