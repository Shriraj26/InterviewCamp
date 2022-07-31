"""
In this case, we have to evaluate a infix expression with brackets...
Like - (1 + 2 ) / 1 + (3 * 2)
This is very same as the previous stuff!!! whenever u encounter ( then add it to operator stack, and then when u encounter a
) then process everything till u get a (, and then later on pop the ( bracket...

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
myDict = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0, ')': 0}


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

        # print(operatorStack.stack, operandStack.stack)
        # If u get an operand, just push it
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            operandStack.push(int(i))

        elif i == '(':
            operatorStack.push(i)

        elif i == ')':
            while not(operatorStack.isEmpty()) and operatorStack.top() != '(':
                process()
            operatorStack.pop()

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

    # process the last operands
    while not (operatorStack.isEmpty()):

        if len(operandStack.stack) == 1:
            break

        process()

    print('Final - ', operandStack.stack)


processString()
