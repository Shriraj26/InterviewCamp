"""
U can have one array that will be used to implement 2 stacks... In this case the starting index will represent the stack S1 and the
ending index will represent the index S2, increment S1 to push element for S1, and decrement S2 to push an element in S2
By this case we have like 2 pointers that will act as the TOP elements of stacks...

U can also use single array to implement 3 stacks as well... Just divide array into 3 equal parts and then u can proceed...

Input - just give array as space separated integers 1 2 3 4 5

"""


class StackUsingArray:

    def __init__(self, n):
        self.arr = [None for i in range(n)]
        self.S1 = 0
        self.S2 = n-1


    def push(self, elem, whereTo):
        if self.S1 > self.S2 or self.S1 == len(self.arr) or self.S2 < 0:
            print(' Cannot push, overflow! ')
            return

        if whereTo == 'S1':
            self.arr[self.S1] = elem
            self.S1 += 1
        else:
            self.arr[self.S2] = elem
            self.S2 -= 1

    def pop(self, whereFrom):

        elem = None
        if whereFrom == 'S1':
            if self.S1 == 0:
                print('Underflow, cannot pop ')
                return
            self.S1 -= 1
            elem = self.arr[self.S1]
            self.arr[self.S1] = None

        else:
            if self.S2 == len(self.arr):
                print('Underflow, cannot pop ')
                return
            self.S2 += 1
            elem = self.arr[self.S2]
            self.arr[self.S2] = None


        return elem

arr = [int(x) for x in input().split()]

stackArr = StackUsingArray(len(arr))

for i in arr:
    stackArr.push(i, 'S2')

print(stackArr.arr)
#print(stackArr.S1)

print(stackArr.pop('S2'))
#print(stackArr.S1)
print(stackArr.arr)

print(stackArr.pop('S2'))
print(stackArr.arr)

print(stackArr.push(59, 'S1'))
print(stackArr.arr)

print(stackArr.push(60, 'S1'))
print(stackArr.arr)

print(stackArr.push(61, 'S1'))
print(stackArr.arr)