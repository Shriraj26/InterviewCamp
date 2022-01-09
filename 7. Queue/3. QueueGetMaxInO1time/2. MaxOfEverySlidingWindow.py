"""
Maximum of Sliding Window: Given an array A and an integer K, find the maximum element in each sliding window of size K. For example:

A = [4,6,5,2,4,7] and K = 3, windows are as follows:

[4,6,5,2,4,7] : Max = 6
[4,6,5,2,4,7] : Max = 6
[4,6,5,2,4,7] : Max = 5
[4,6,5,2,4,7] : Max = 7

Output: 6,6,5,7



"""
class QueueUsingArray:

    def __init__(self, n):
        self.q = [None for i in range(n)]
        self.length = 0
        self.capacity = n
        self.front = 0
        self.back = 0

    def isFull(self):
        if self.length == self.capacity:
            return True
        return False

    def enqueue(self, data):
        if self.isFull():
            return

        self.q[self.back] = data
        self.back = (self.back + 1) % self.capacity
        self.length += 1


    def deqeue(self):
        if self.length == 0:
            print('Cannot dequeue as len is 0 ')
            return

        elem = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.length -= 1
        return elem

    def isEmpty(self):
        return self.length == 0

    def getLast(self):

        if self.back == 0:
            return self.q[self.capacity - 1]
        return self.q[self.back - 1]

    def getFront(self):
        return self.q[self.front]

    def removeLast(self):
        if self.length == 0:
            return

        elem = self.getLast()
        if self.back == 0:
            self.back = self.capacity - 1
        else:
            self.back -= 1

        self.length -= 1

        return elem


class MaxQueue:

    def __init__(self, n):
        self.maxQ = QueueUsingArray(n)
        self.queue = QueueUsingArray(n)

    def getMax(self):

        if self.maxQ.length == 0:
            print('Queue empty, add elem to get max ')
            return
        print(self.queue.q , self.maxQ.q, end = ' ')
        return self.maxQ.q[self.maxQ.front]

    def enqueue(self, elem):

        self.queue.enqueue(elem)
        while not(self.maxQ.isEmpty()) and self.maxQ.getLast() < elem:
            self.maxQ.removeLast()

        self.maxQ.enqueue(elem)


    def isFull(self):
        return self.queue.isFull()


    def dequeue(self):

        if self.maxQ.getFront() == self.queue.getFront():
            self.maxQ.deqeue()

        self.queue.deqeue()



k = int(input('Enter the size of sliding window '))
m = MaxQueue(k)

print('Enter the elems in the queue ')
arr = [int(x) for x in input().split()]

for i in arr:
    if m.isFull():
        print(m.getMax())
        m.dequeue()
    m.enqueue(i)

# To get the last elem in the window...
print(m.getMax())



# 9 7 0 4 6 2 7 4





