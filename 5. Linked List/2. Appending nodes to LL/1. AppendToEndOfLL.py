"""
Given a node X, and head and tail pointers to a LL, append that node to its end

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def createLL(self, arr):

        for i in arr:
            newNode = Node(i)
            if self.head is None:
                self.head = newNode
                self.tail = newNode

            else:
                self.tail.next = newNode
                self.tail = self.tail.next

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()

    def appendNode(self, node):

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next



arr = [int(x) for x in input().split()]
inpLL = LinkedList()
inpLL.createLL(arr)
inpLL.printLL()
X = Node(int(input('enter the data for node u want to create -  ')))
inpLL.appendNode(X)

inpLL.printLL()