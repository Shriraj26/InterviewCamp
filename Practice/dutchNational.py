arr = [int(x) for x in input().split()]
pivot = int(input())

s = 0
l = len(arr) - 1
i = 0

while i <= l:

    if arr[i] < pivot:
        arr[i], arr[s] = arr[s], arr[i]
        s += 1
        i += 1

    elif arr[i] > pivot:
        arr[i], arr[l] = arr[l], arr[i]
        l -= 1
    else:
        i += 1

print(arr)

