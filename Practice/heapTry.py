import heapq
def topKLargest():

    minHeap = []
    for i in range(len(arr)):
        heapq.heappush(minHeap, (-arr[i], i))

    count = 0

    finalArr = []
    bigArr = []
    smallArr = []

    for i in range(bigHits):

        if -minHeap[0][0] > bigHits:
            print('arr i and minHeap 0 ',arr[i], minHeap[0])    
            if arr[i] >= -minHeap[0][0]:
                elem = heapq.heappop(minHeap)
                # print('Popped elem ', elem)            
                count += 1
                bigArr.append(-elem[1] + 1)
    
    while len(minHeap) > 0:
        elem = heapq.heappop(minHeap)
        print('popped nexr - ', elem)
        count = count - elem[0]
        smallArr.append(-elem[1] + 1)

    print(count)
    finalArr.append([count])
    
    if len(bigArr) == 0:
        finalArr.append([-1])
    else:
        finalArr.append(bigArr)

    finalArr.append(smallArr)
    
    print(finalArr)

bigHits = int(input())
arr= [int(x) for x in input().split()]
topKLargest()


def smashTheBricks(bigHitsCount, newtons) :
    arrWithIndex = []
    bigHits,smallHits = [],[]
    for index,values in enumerate(newtons) :
        arrWithIndex.append((values,index + 1))
        
    arrWithIndex = sorted(arrWithIndex, 
       key=lambda x: x[0], reverse=True)
       
    minHits = 0
    current = 1
    print(arrWithIndex)
    for i in range(len(arrWithIndex)) :
        if (bigHitsCount > 0 ) :
            bigHits.append(arrWithIndex[i][1])
            bigHitsCount -= 1
            minHits += 1
        else :
            smallHits.append(arrWithIndex[i][1])
            minHits += arrWithIndex[i][0]
        
    return( [[minHits],sorted(bigHits), sorted(smallHits)])