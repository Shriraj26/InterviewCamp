"""
In arrays we did sort 0 1 2 based on the dutch national flag algorithm, here we need to sort the nodes that have values 0 1 2
So here, we will create 3 pointers one for 0, one for 1 and one for 3, then we will keep on deleting nodes from
LL and appending it to the respective pointers, and finally append 0, 1 and 2 pointers to each other!!
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

