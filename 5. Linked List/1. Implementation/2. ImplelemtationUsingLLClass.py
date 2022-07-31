"""
Linked List implementation using a class...
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
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def createLL(self, arr):

        temp = None
        for i in arr:
            newNode = Node(i)
            self.appendNode(newNode)

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()



arr = [int(x) for x in input().split()]

linkedListObject = LinkedList()
linkedListObject.createLL(arr)
linkedListObject.printLL()

