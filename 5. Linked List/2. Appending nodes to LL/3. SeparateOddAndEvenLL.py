"""
odd and even LL are based on its position and not by its Value!!! so consider the indices here!!
Given a Linked List L, separate it into 2 Linked Lists. One contains L's odd nodes and the other contains L's even nodes. For example:

Input: Head -> 1 -> 2 -> 3 -> 4 -> 5

Result 1: Head -> 1 -> 3 -> 5
Result 2: Head -> 2 -> 4

Note: Odd and Even here refer to the node's position, not value.
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def appendNode(self,node):

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = self.tail.next

    def createLL(self, arr):

        for i in arr:

            newNode = Node(i)
            self.appendNode(newNode)

    def printLL(self):

        temp = self.head
        while temp is not None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()

def separateOddEven(inputLL):

    odd = LinkedList()
    even = LinkedList()

    temp = inputLL.head

    count = 0
    while temp is not None:

        if count % 2 == 0:
            even.appendNode(temp)
        else:
            odd.appendNode(temp)

        temp = temp.next
        count += 1

    # Now separate the tail's next pointers
    if odd.tail is not None:
        odd.tail.next = None
    if even.tail is not None:
        even.tail.next = None

    return odd, even



arr = [int(x) for x in input().split()]

inputLL = LinkedList()
inputLL.createLL(arr)

odd, even = separateOddEven(inputLL)

print('Odd - ')
odd.printLL()
print('Even - ')
even.printLL()