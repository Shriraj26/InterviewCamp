arr = [int(x) for x in input().split()]
k = int(input())
buff = [None] * k

def processBuffer(startINdex, bufferINdex):

    if bufferINdex == len(buff):
        print(buff)
        return

    if startINdex == len(arr):
        return

    for i in range(startINdex, len(arr)):
        buff[bufferINdex] = arr[i]
        processBuffer(i+1, bufferINdex+1)


processBuffer(0 ,0)




