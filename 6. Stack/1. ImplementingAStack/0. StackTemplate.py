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
