"""
This is some different magic that we are going to do here...
To check Palindrome, we follow these steps -
1. Find Median of the linked list
2. reverse the ll after the median.. ex - A->B->C->B->A  --->   A->B->C<-B<-A
        for even -  A->B<-B<-A
3. then point start to start and end to end
4. Traverse and check if start == end, if not then exit
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(node):
    temp = node
    while temp is not None:
        print(temp.data, end=' ')
        temp = temp.next


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
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        middleVal = count // 2

        prev = None
        curr = self.head
        while middleVal > 0:
            prev = curr
            curr = curr.next
            middleVal -= 1
        if count % 2 == 0:
            return prev
        return curr

    def reverseLL(self, middle):

        prev = middle
        curr = middle.next
        middle.next = None

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def isPalindrome(self):

        median = self.getMedian()

        start = self.head
        end = self.reverseLL(median)

        while start is not None and end is not None:

            if start.data != end.data:
                return False

            start = start.next
            end = end.next

        return True


arr = [int(x) for x in input().split()]

inputLL = LinkedList()
inputLL.createLL(arr)

# medianNode = inputLL.getMedian()
# print('median is at - ',medianNode.data)

print(inputLL.isPalindrome())
