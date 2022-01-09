"""
Print all combinations of length 3.
If u have an array - 1,2,3,4,5,6  We need all the combinations or selections of array of length 3
Ex - 1,2,3 ... 1 2 3... 3,4,5 ... 4 5 6  etc
We will be doing this by using an Auxillary buffer.. this is a temporary buffer that we will be using for our purpose

To Remember -
1. Buffer madhe bhar
2. Sagle combinations de mala, ha i+1 kar karan repetitions nakoyet
3. Jeva len 3 hoil teva print kar

"""


arr = [int(x) for x in input().split()]
bufferArr = [None, None, None]

def printAllCombos(startIndex, bufferIndex):

    # Base case 1 when buffer index goes out of range
    if bufferIndex == len(bufferArr):
        print(bufferArr)
        return

    # base case 2 when the actual array goes out of range
    if startIndex == len(arr):
        return

    # loop through the array and one by one generate all the combinations for the buffer
    for i in range(startIndex, len(arr)):
        bufferArr[bufferIndex] = arr[i]

        # call the printAllCombos for the i+1 index
        # print('Calling for ')
        printAllCombos(i+1, bufferIndex+1)


printAllCombos(0, 0)