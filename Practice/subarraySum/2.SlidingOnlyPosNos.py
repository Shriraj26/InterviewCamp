arr = [int(x) for x in input().split()]

k = int(input())
final = []
def func():

    start = 0
    end = 0
    windowSum = arr[start]

    while start < len(arr):

        if start > end:
            end = start
            windowSum = arr[start]

        if windowSum < k:

            if end == len(arr) - 1:
                break
            end += 1
            windowSum += arr[end]

        elif windowSum > k:
            windowSum -= arr[start]
            start += 1

        else:
            final.append(start)
            final.append(end)
            break

    print(final)
func()


