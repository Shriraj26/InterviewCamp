import heapq
"""
In this we will get the K largest elements in the array using the Heap, we will
1. Create a min heap of size K
2. Add elements (first K elems)
3. From K+ 1 till end of array, compare top of heap with array elem, if top is smaller than array elem, delete top
    from heap and add array elem
4. Do this for all elems in the array.
5. at last u have got k Largest elements in the heap!! pop all to get those!!
"""

print('Enter the elems in the array ')
arr = [int(x) for x in input().split()]
k = int(input('Enter the value of K'))

# By default, heapq creates a minheap!!
# steps are - create an array of size k, pass it to heapify funciton then you are done
def topKLargest():

    # Create a heap
    minHeap = [arr[i] for i in range(k)]

    # init the heap, this does not return anythong take that into mind
    heapq.heapify(minHeap)

    for i in range(k+1, len(arr)):

        if arr[i] >= minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, arr[i])


    print(minHeap)


topKLargest()

