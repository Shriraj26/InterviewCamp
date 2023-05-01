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

    def getCycleLength(self):
        slow = self.head
        fast = self.head

        while fast is not None:

            fast = fast.next
            if fast == slow:
                break

            if fast is not None:
                fast = fast.next
                if fast == slow:
                    break
            slow = slow.next

        # no cycle, return -1
        if fast is None:
            return -1

        # now if there is a cycle
        count = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            count += 1

        return count


arr = [int(x) for x in input().split()]

inputLL = LinkedList()
inputLL.createLL(arr)
index = int(input('Enter the index that u want tail to join to to form cycle '))

node = inputLL.getNode(index)

# Join the tail to the node to form a cycle, if u comment this line, then it will give u false
inputLL.tail.next = node

print('Length of cycle - ', inputLL.getCycleLength())
