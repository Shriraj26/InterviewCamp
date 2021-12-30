"""
Print all permutations of length X.

We have already covered combinations. We now use the same technique to generate permutations.
Ex - 1,2,3,4,5 and X is 3 there fore our ans will have -
1,2,3  ... 1 3 2 ........ 3 4 5... 5 4 3
This is very similar to the 1st problem that we had done,
In the first prolem, we included a number and then looked for i+1
say 1,2,3,4,5 .. if we had 1 and 3 in the buffer, then we looked for elements after 3 that are 4,5
But for permutations, we need to include elements that are not already included in the buffer
say if 1 and 3 are there in buffer, 1 3 2 is also a case... Therefore, we include a flag to check that number is already
present in the buffer or not... If not then include it in the buffer, if yes the ignore
Afrer we process that element, we will mark that flag as false
"""

arr = [int(x) for x in input().split()]

bufferArr = [None, None, None]
isIncludedInBuffer = [False for x in range(len(arr))]


def permutationsOfArray(bufferIndex):

    # as we don't have startIndex of array in input, we have only one termination case that if buffer is full then
    # return
    if bufferIndex == len(bufferArr):
        print(bufferArr)
        return

    for i in range(len(arr)):

        # if the array element is not included in the buffer then only include it
        if isIncludedInBuffer[i] is False:
            bufferArr[bufferIndex] = arr[i]
            # now that we have included it, mark it as true
            isIncludedInBuffer[i] = True

            # recursively call the next indices to fill the buffer array
            permutationsOfArray(bufferIndex + 1)

            # now that we processed the index, mark it again as false
            isIncludedInBuffer[i] = False

    pass


permutationsOfArray(0)
