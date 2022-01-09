"""
A Queue is a FIFO DS with 2 functions, enqueue - add to queue or dequeue pop from queue...
A Queue can be implemented using -
1. Linked List
2. Arrays..

Using LL is quite simple, just get a head node and a tail node, and then keep on adding the new nodes for the enqueue
functionality... For the dequeue, just do head = head.next

To implement using an Arrray, we will use it in a circular manner!!! when index reaches end, and if there is space,
in front, then the index will again appear at the front... the tequnique is that index = (index+1) % len(of array)
By this method, the index circles around the array , from 0 to len array -1 to again 0 and so on
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
            print('Queue Full, cannot enqueue ')
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

    def getLast(self):

        if self.back == 0:
            return self.q[self.capacity - 1]
        return self.q[self.back - 1]

    def getFront(self):
        return self.q[self.front]

print('Enter the elements u want in the queue ')
arr = [int(x) for x in input().split()]

# initialize the queue
Q = QueueUsingArray(len(arr))

# Fill the elements
for i in arr:
    Q.enqueue(i)

# print(Q.q, Q.front, Q.back)

Q.deqeue()
Q.deqeue()
Q.deqeue()
Q.enqueue(100)
Q.enqueue(101)
Q.enqueue(102)
print(Q.q)
print(Q.q[Q.front])

