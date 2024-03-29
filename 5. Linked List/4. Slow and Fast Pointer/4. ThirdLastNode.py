"""
A similar application of slow and fast pointer is to get the third last elem from the LL, u can have one pointer assigned to the
head node, and second pointer assigned to the 3rd node, by the time second pointer reaches the end, the first pointer
reached the third last element of the LL, thus u get the result that way
the speed of advancement of the pointers is the same, each advances one by one

Refer the nth last node for the solution... its better than this...
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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

    def thirdLastElem(self):

        first = self.head
        second = self.head

        if second is not None:
            second = second.next
            if second is not None:
                second = second.next
            else:
                return None
        else:
            return None

        if second is not None:

            while second.next is not None:

                second = second.next
                first = first.next

            return first
        else:
            return None





arr = [int(x) for x in input().split()]

inputLL = LinkedList()
inputLL.createLL(arr)


medianNode = inputLL.thirdLastElem()
if medianNode is None:
    print('No third last elem ')
else:
    print('third last is at - ',medianNode.data)