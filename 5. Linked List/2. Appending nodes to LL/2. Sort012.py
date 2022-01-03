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

def appendList(toAppend, original):

    if toAppend is None or toAppend.head is None:
        return
    original.appendNode(toAppend.head)
    original.tail = toAppend.tail


def sort012(node0, node1, node2, inputLLObject):
    current = inputLLObject.head

    while current is not None:
        if current.data == 0:
            node0.appendNode(current)
        elif current.data == 1:
            node1.appendNode(current)
        else:
            node2.appendNode(current)

        current = current.next

    # Now the tail's Next will have the extra data that we have to set it as None
    if node0.tail is not None:
        node0.tail.next = None
    if node1.tail is not None:
        node1.tail.next = None
    if node2.tail is not None:
        node2.tail.next = None

    # Now point node0 to node1 and node1 to node2
    result = LinkedList()
    appendList(node0, result)
    appendList(node1, result)
    appendList(node2, result)

    # Finally return the result node
    return result





arr = [int(x) for x in input().split()]

#Create the input linked List of 0s and 1s
inputLLObject = LinkedList()
inputLLObject.createLL(arr)

# Create 3 separate pointers for 0,1,2
node0 = LinkedList()
node1 = LinkedList()
node2 = LinkedList()

# Call the sort function
newNode = sort012(node0, node1, node2, inputLLObject)
newNode.printLL()
