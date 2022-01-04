"""
Given a Linked List Node, detect whether there exists a cycle in it or not
Now programatically, to find a cycle we need an input of LL that actually has a cycle, thus we will take an
index as input, now the tail will be connected to this index...
say - 0 1 2 3 4 5 6... and u gave the index input as - 3, thus out LL will become - 0 1 2 3 4 5 6 3 4 ....
Meaninng, 6 is connected to node 3 again forming cycle 3 4 5 5
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

    def getNode(self, n):
        temp = self.head
        for i in range(n):
            temp = temp.next
        return temp

    def hasCycle(self):

        slow = self.head
        fast = self.head

        while fast is not None:

            fast = fast.next
            if fast == slow:
                return True

            if fast is not None:
                fast = fast.next
                if fast == slow:
                    return True
            slow = slow.next
        return False


arr = [int(x) for x in input().split()]

inputLL = LinkedList()
inputLL.createLL(arr)
index = int(input('Enter the index that u want tail to join to to form cycle '))

node = inputLL.getNode(index)

# Join the tail to the node to form a cycle, if u comment this line, then it will give u false
inputLL.tail.next = node

print(inputLL.hasCycle())