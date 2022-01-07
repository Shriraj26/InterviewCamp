"""
In this case, we have to evaluate a infix expression, this is like a regular expression without prantheses...
Like - 1 + 2 / 1 + 3 * 2
In this case, we will follow the operator priority where, * or / have same priority and they have more priority than the
- or +
We will mantain 2 stacks for this, one for operands - 1 2 3 ... and one for operators - + / *
there are cases that we need to follow -
1. if char at i is a number, push it to operand
2. If the char at i is operator, then if operator stack is empty, push that operator
3. if char at i is operator and if operator stack is not empty -
    1. if char at i is / or * and operator stack top has + or - , meaning, the operator stack top has less priority than the
        char at i, push the char at i to the op stack
    2. if char ar i is + or - and the operator stack top has priority greater than or equal to op, then process the stack.
        In process, we remove 2 elems from operand stack, then perform operation that the top of operator stack has and
        push it back..
4. In the end, we have to again process the elements till single element remains in the operand stack
"""
import sys


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


operatorStack = Stack(sys.maxsize)
operandStack = Stack(sys.maxsize)

s = input()
myDict = {'+': 1, '-': 1, '/': 2, '*': 2}


def process():
    top = 0
    bot = 0
    op = '+'
    result = 0
    if not (operandStack.isEmpty()):
        bot = operandStack.pop()
    else:
        print('elems should be there in stack to pop,input is wrong 1')
        return

    if not (operandStack.isEmpty()):
        top = operandStack.pop()
    else:
        print('elems should be there in stack to pop,input is wrong 2')
        return

    if not (operatorStack.isEmpty()):
        op = operatorStack.pop()
    else:
        print('operator elems should be there in stack to pop,input is wrong 3')
        return

    if op == '+':
        result = top + bot
    elif op == '-':
        result = top - bot
    elif op == '*':
        result = top * bot
    elif op == '/':
        result = top // bot

    operandStack.push(result)


def processString():
    for i in s:

        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:

            operandStack.push(int(i))

        else:
            if operatorStack.isEmpty():

                operatorStack.push(i)
            else:
                top = operatorStack.top()

                # if the top of stack has greater or equal priority
                if myDict[top] >= myDict[i]:

                    while not (operatorStack.isEmpty()) and myDict[operatorStack.top()] >= myDict[i]:
                        process()

                    operatorStack.push(i)
                else:
                    operatorStack.push(i)

    while not (operandStack.isEmpty()):

        if len(operandStack.stack) == 1:
            break

        process()

    print('Final - ', operandStack.stack)


processString()
