"""
Reverse a Linked List

Don't think about recursion... Just do it in a new way, keep 3 pointers, prev, curr and next
Point prev to None initially, curr to head and next to head.next
then assign curr.next to prev, and advance
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def appendNode(self, node):

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
            print(temp.data, end=' ')
            temp = temp.next
        print()


    def reverseLL(self):

        prev = None
        curr = self.head

        while curr is not None:

            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode


        return prev

arr = [int(x) for x in input().split()]

ipLL = LinkedList()
ipLL.createLL(arr)
newHead = ipLL.reverseLL()

while newHead is not None:
    print(newHead.data, end = ' ')
    newHead = newHead.next