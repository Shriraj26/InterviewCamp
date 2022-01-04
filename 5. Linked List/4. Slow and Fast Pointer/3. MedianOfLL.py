"""
Find median of a Linked List, u can do this by the same method of fast and slow pointers, advance fast pointer and slow pointer
advance fast pointer till it reaches the end
By that time, the slow pointer might have reached the mid point of the Linked List as the slow pointer travels half the speed
of the fast pointers
Please give odd length input as LL, then u will get the answer

"""

"""
Given a Linked List Node, detect whether there exists a cycle in it or not
Now the LL can have a cycle, the approach is fairly simple, advance fast and slow pointers till they meet, once they meet,
then only advance fast pointer one by one till it meets slow pointer again, then count nodes along the way...
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

    def getMedian(self):

        slow = self.head
        fast = self.head


        while fast.next is not None:

            fast = fast.next
            fast = fast.next
            slow = slow.next

        return slow


arr = [int(x) for x in input().split()]

inputLL = LinkedList()
inputLL.createLL(arr)


medianNode = inputLL.getMedian()
print('median is at - ',medianNode.data)