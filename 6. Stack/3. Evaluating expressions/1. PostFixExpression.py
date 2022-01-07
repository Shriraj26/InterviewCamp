"""
In this case we will evaluate something like this -  1 5 + 2 -
This means that we will do - 1 + 5 - 2
In this type of cases, the operator is after the numbers and we have to interprate it that way...
The algo is fairly simple, push elements into stack when numbers are encountered, if u get any operand, then
pop 2 elements, perform the operation , push the result back to the stack...
Input - 1 5 + 2 -  ... dont give brackets in this...
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



expression = [x for x in input().split()]
S = Stack(2)


def processOperator(operator):

    # pop 2 elements from the stack
    if not(S.isEmpty()):
        top = S.pop()
    else:
        print('Problem in the input expresion, stack empty cannot pop ')
        return -1

    if not (S.isEmpty()):
        bot = S.pop()
    else:
        print('Problem in the input expresion, stack empty cannot pop ')
        return  -1

    result = 0
    if operator == '+':
        result = bot + top
    if operator == '-':
        result = bot - top
    if operator == '*':
        result = bot * top
    if operator == '/':
        result = bot + top


    # put back result into the stack
    S.push(result)

    return 0


def evaluate(expression):

    for i in expression:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7' ,'8', '9']:
            S.push(int(i))
        else:
            processOperator(i)

    print(S.stack)


evaluate(expression)