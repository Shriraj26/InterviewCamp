
arr = [int(x) for x in input().split()]
maxArea = - float('inf')
left = 0
right = len(arr ) -1

while left < right:

    area = (right - left) * min(arr[left], arr[right])
    maxArea = max(area, maxArea)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

    print(arr[left], arr[right], maxArea)

