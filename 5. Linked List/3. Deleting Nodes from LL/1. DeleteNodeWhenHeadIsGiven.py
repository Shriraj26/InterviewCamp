"""
U are given a head, now your task is to delete a given node...
The approach is simple,
1. If the node to delete is the head node, just point head to haed.next
2. if the node to delete is either in between or is a tail node, then find prev node, and point it to the next of
    node to delete
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

    def getPrev(self, node):

        prev = self.head
        while prev.next != node:
            prev = prev.next
        print()
        return prev

    # This function is just to provide the particular node that u want to delete, just provide the index
    def getNode(self, n):
        temp = self.head
        for i in range(n):
            temp = temp.next
        return temp

    def deleteNode(self, node):
        if node == self.head:
            self.head = self.head.next
        else:
            prev = self.getPrev(node)
            prev.next = node.next

arr = [int(x) for x in input().split()]

inputLl = LinkedList()
inputLl.createLL(arr)

n = int(input('Enter the index which node u want to delete, please let it be in bounds!! '))

nodeToDelete = inputLl.getNode(n)
inputLl.deleteNode(nodeToDelete)

inputLl.printLL()





