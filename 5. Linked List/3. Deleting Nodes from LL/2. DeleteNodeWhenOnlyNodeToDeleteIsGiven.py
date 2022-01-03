"""
Let's say you are not given N's previous node. Is there another way to delete N?
This approach u should now remember by heart, to delete the given node, where prev or head is not given,
u just need to rememver this ---- Copy!!!!!!
1. Copy the node to delete's all the next nodes till end's value in the node to delete
2. then delete the last node!!!

Note --- it is the case that the node to be deleted will not be the tail node in the lInked list!!1
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
        currPointer = node
        nextPointer = node.next

        while nextPointer.next is not None:
            currPointer.data = nextPointer.data
            currPointer = nextPointer
            nextPointer = nextPointer.next

        currPointer.data = nextPointer.data
        currPointer.next = None

arr = [int(x) for x in input().split()]

inputLl = LinkedList()
inputLl.createLL(arr)

n = int(input('Enter the index which node u want to delete, please let it be in bounds!! '))

nodeToDelete = inputLl.getNode(n)
inputLl.deleteNode(nodeToDelete)

inputLl.printLL()






