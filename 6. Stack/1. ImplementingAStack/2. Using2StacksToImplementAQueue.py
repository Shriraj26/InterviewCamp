"""
Consider 2 stacks S1 and S2...
There are 2 ways of doing this -
1. Enqueue takes O(1) time and dequeue takes O(N) time...
    Enqueue means pushing into the queue right, so in this case we keep on pushing normally into the stack S1.
    When it comes to dequeing, now actually we want to bottom element of the stack as it came first, therefire we
    pop all the elements from S1 and then push it onto S2, then we return the top element of S2 as now the bottom elem
    from S1 will be the top element of S2!!! THus Enqueue takes O(1) time and dequeue takes O(N) time
2. Enqueue takes O(N) time and dequeue takes O(1) time...
    in this case, s1 always gets the elements in queue order, to do that, if there are say 2 elements in S1, if new elem
    comes in, we pop all the elements from the S1 and push it into S2, and then add new elem to S1, then we bring back all
    the elements from S2 to S1 agani... thus Enqueue takes O(N) time and dequeue takes O(1) time

Input - 1 2 3 4 5

"""

class Stack:

    def __init__(self, n):
        self.stack = []
        self.capacity = n

    def push(self, elem):
        if self.isFull():
            print('Stack full cannot push')
            return
        self.stack.append(elem)

    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            print('Stack empty, Cannot Pop')
            return
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity


class QueueUsingStack:

    def __init__(self, n):
        self.S1 = Stack(n)
        self.S2 = Stack(n)
        self.capacity = n

    def enqueue_method_1(self, elem):
        self.S1.push(elem)

    def dequeue_method_1(self):

        # if both the queues are empty it means that no elem present so nothing to dequeue
        if self.S1.isEmpty() and self.S2.isEmpty():
            return -1

        # if S2 is empty then push all elem to S2 from S1
        if self.S2.isEmpty():
            while not(self.S1.isEmpty()):
                self.S2.push(self.S1.pop())

        # return top of S2
        return self.S2.pop()

    def enqueue_method_2(self, elem):

        # pop all the elements at first from S1, put it into S2
        if not(self.S1.isEmpty()):
            while not(self.S1.isEmpty()):
                self.S2.push(self.S1.pop())

        # add the latest elem, this will now go to the bottom of S1
        self.S1.push(elem)

        # pop all added elements from S2 and add it back to S1
        while not (self.S2.isEmpty()):
            self.S1.push(self.S2.pop())



    def dequeue_method_2(self):

        if self.S1.isEmpty():
            return -1

        return self.S1.pop()


arr = [int(x) for x in input().split()]
Q = QueueUsingStack(len(arr))

for i in arr:
    # u can use either methods here 1 or 2
    Q.enqueue_method_1(i)


#Function calls using method 1
print(Q.dequeue_method_1())
print(Q.S1.stack)
print(Q.S2.stack)
print(Q.dequeue_method_1())
print(Q.S1.stack)
print(Q.S2.stack)

# Function calls using method 2
# print(Q.dequeue_method_2())
# print(Q.S1.stack)
# print(Q.S2.stack)
# print(Q.dequeue_method_2())
# print(Q.S1.stack)
# print(Q.S2.stack)


