"""
Implement a stack and find if an elem exists in a stack or not...
Here we will be using a temp stack to push the elements of original stack until we get an element... if we get it then we break
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


def checkIfElemExists(elem, S):
    temp = Stack(len(S.stack))
    ifELemExists = False
    while not (S.isEmpty()):
        top = S.top()
        if top == elem:
            print('Got the elem ')
            ifELemExists = True
            break
        temp.push(S.pop())



    # push back the temp elements back to the original stack
    while not (temp.isEmpty()):
        S.push(temp.pop())

    return ifELemExists


arr = [int(x) for x in input().split()]
elem = int(input('Enter elem to find in the stack - '))
S = Stack(len(arr))
for i in arr:
    S.push(i)

print(checkIfElemExists(elem, S))
