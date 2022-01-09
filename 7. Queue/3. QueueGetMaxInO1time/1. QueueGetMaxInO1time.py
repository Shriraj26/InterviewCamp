"""
Now we need to implement a queue that will take O(1) time to fetch max for us...
The approach here is simple, in stack u used 2 stacks, one for all the elems and one for the newer ones that came, same u will be
doing for the queue.. one queue for the elems and one for mantaining the max elem yet..
In case of stack, we needed to mantain a history of the elements appeared in the stack, but in queue, this will not be the case,
we will only keep track of the elements that are greater than the front of the queue
For ex currently the queue has - 1,4,2,3 then our max queue will have - 4,3 ... as 1, 2 are not needed
Why?
because, when we dequeue, 1 and 2 might get removed from the queue first and not 4 and 3 as in case of the stack,
4 and 3 might get removed before..., thus we dont care about them
When we append to queue we check -
while back of max queue less than the elem to be added,
    remove from back of queue
For dequeue we do -
while if max.fromt == elem to be removed,
    max.dequeue
q.dequeue


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


    def isEmpty(self):
        return self.length == 0

    def getLast(self):

        if self.back == 0:
            return self.q[self.capacity - 1]
        return self.q[self.back - 1]

    def getFront(self):
        return self.q[self.front]




class MaxQueue:

    def __init__(self, n):
        self.maxQ = QueueUsingArray(n)
        self.queue = QueueUsingArray(n)

    def getMax(self):

        if self.maxQ.length == 0:
            print('Queue empty, add elem to get max ')
            return

        return self.maxQ.q[self.maxQ.front]

    def enqueue(self, elem):
        self.queue.enqueue(elem)

        while not(self.maxQ.isEmpty()) and self.maxQ.getLast() < elem:

            # need to dequeue from back!!
            self.maxQ.removeLast()


        self.maxQ.enqueue(elem)



    def dequeue(self):

        if self.maxQ.front == self.queue.front:
            self.maxQ.deqeue()

        self.queue.deqeue()


m = MaxQueue(10)

m.enqueue(9)
m.enqueue(7)
m.enqueue(0)
m.enqueue(4)
print('Max yet is - ',m.getMax())
m.enqueue(100)

m.enqueue(20)
print('Max yet is - ',m.getMax())
m.enqueue(4)
m.enqueue(777)
print('Max yet is - ',m.getMax())


