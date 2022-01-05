"""
Implement a Stack with O(1) lookup of the maximum element in the stack. For example,

Stack: 3 -> 2 -> 1 -> 5
Max() => 5

After 1 pop():
Stack: 3 -> 2 -> 1
Max() => 3

The approach is simple, use a stack for max as well, push the maximum elements on the max stack only, say if a elem
comes into the stack, if it is less than the top of maxStack, then dont push it into the stack!!

Input - just give array as space separated integers
"""

class Stack:

    def __init__(self, n):
        self.stack = []
        self.max = []
        self.capacity = n

    def push(self, elem):
        if self.isFull():
            print('Stack full cannot push')
            return
        self.stack.append(elem)

        if len(self.max) == 0 or self.max[-1] < elem:
            self.max.append(elem)

    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            print('Stack empty, Cannot Pop')
            return

        if self.top() == self.max[-1]:
            self.max.pop()
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity


    def getMax(self):
        return self.max[-1]

arr = [int(x) for x in input().split()]
stk = Stack(len(arr))

# fill the stack
for i in arr:
    stk.push(i)

print(stk.stack, stk.max)
print('Max in the entire stack is - ', stk.getMax())

