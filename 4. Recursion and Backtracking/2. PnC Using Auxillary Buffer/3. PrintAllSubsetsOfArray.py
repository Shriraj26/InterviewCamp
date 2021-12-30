"""
Print all subsets of an array of integers.

We solve this by modifying one line in the solution for printing combinations. as discussed in problem 1
This really shows how you can use Building Blocks for one problem to solve different problems.
We have just changed one line where we wanted to print the buffer array... And thats it!! it does the job!
We are printing just when we wnter the function and till the bufferindex(not including it) as bufferindex
will get filled later onwards!!
"""


arr = [int(x) for x in input().split()]
bufferArr = [None, None, None]

def printAllSubsets(startIndex, bufferIndex):

    printArray(bufferArr, bufferIndex)
    # Base case 1 when buffer index goes out of range
    if bufferIndex == len(bufferArr):
        # Instead of printing here we will print at Top
        # print(bufferArr)
        return

    # base case 2 when the actual array goes out of range
    if startIndex == len(arr):
        return

    # loop through the array and one by one generate all the combinations for the buffer
    for i in range(startIndex, len(arr)):
        bufferArr[bufferIndex] = arr[i]

        # call the printAllCombos for the i+1 index
        # print('Calling for ')
        printAllSubsets(i+1, bufferIndex+1)

def printArray(arr, index):

    print(arr[0: index])

printAllSubsets(0, 0)