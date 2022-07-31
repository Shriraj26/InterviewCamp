"""
1. We will use the 2nd approach of the top K elements where first we create the heap of k elements
    then one by one pop elements and push other depending on their value or priority
2. Now, our priority here is the count of the occurrences of the elements in the array, the dict
    will store the occurrences for us.
3. Now, for count K create a heap and add the elements from the dictionary as a tuple...
    if we add tuple [1, 0] in the heap, 1 will be considered as the priority and 0 is the actual
    element, so every time 1 eill be compared for checking the priority
4. After that, as it is a minHeap, low priority elements will be at top, compare it with other
    elements from the dictionary, if their priority is greater the one on top, pop heap and push
    the elemtent from dict... do this till u get over all the elements form the dict...
5. At last the elements in heap will have K most frequent elements,, as we have stored them as a
    tuple, we will use arr as a new arr to store the elements and exclude the priority... and
    return the array finally!!!
"""


import heapq
import collections

print('Enter elems in the array ')
arr = [int(x) for x in input().split()]
k = int(input('Enter the value of k '))

def topKFreq():

    # create a dictionary to store counts
    myDict = collections.Counter(arr)

    # create a min heap
    minHeap = []

    # Heapify it
    heapq.heapify(minHeap)

    # add elems to it as tuple
    count = k
    for key, val in myDict.items():
        if count > 0:
            heapq.heappush(minHeap, (val, key))
        else:
            # check if an element occurred more than top element of the heap, then pop heap and insert it
            if minHeap[0][0] < val:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (val, key))

        count -= 1

    freqElems = [elem[1] for elem in minHeap]

    print('Freq elems are - ')
    print(freqElems)


topKFreq()
