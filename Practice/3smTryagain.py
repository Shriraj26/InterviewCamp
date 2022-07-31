arr = [int(x) for x in input().split()]
res = []
def sum3():

    arr.sort()

    for i in range(len(arr) - 2):

        if i == 0 or (i > 0 and arr[i] != arr[i-1]):

            start = i+1
            end = len(arr) - 1
            while start < end:
                if arr[start] + arr[end] + arr[i] == 0:
                    res.append([arr[i], arr[start], arr[end]])

                    while start < end and arr[start] == arr[start + 1]:
                        start += 1

                    while start < end and arr[end] == arr[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1

                elif arr[start] + arr[end] + arr[i] < 0:
                    start += 1

                else:
                    end -= 1

    print(res)



sum3()
