"""
To implement a LRU Cache, u need to do certain things -
1. Linked list to use will be a doubly linked list, as we have delete operation as well, we need to have this
2. A Hash Table that will have key as the data inside the node, and the value as the node of a linked List itself
3. Functions of LRU Cache -
    1. Read - when u perform read, u look up in hash table to get the node, then pull it out from the LL, append it to end
        as now it will become the most recently used elem now
    2. Write - When u write, check capacity of the CACHE, if it exceeds, delete the least recently used cache, and add the
        new one to the Linked List

"""


# Linked List Node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getPrev(self):
        return self.prev

    def setPrev(self, node):
        self.prev = node

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value


# LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def createLRUFromArray(self, arr):

        # Add the nodes to LL
        for i in arr:
            key = i[0]
            value = i[1]
            newNode = Node(key, value)
            self.appendToLinkedList(newNode)
            self.map[key] = newNode

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.key, temp.value, end=' -> ')
            temp = temp.next
        print()

    def addNode(self, key, value):
        newNode = Node(key, value)
        self.appendToLinkedList(newNode)
        self.map[key] = newNode

    # Append node to the tail of the linked List
    def appendToLinkedList(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.setNext(node)
            node.setPrev(self.tail)

        self.tail = node

    # remove a node from the linked list
    def removeFromLinkedList(self, node):

        if node.getPrev() is not None:
            print('Heree where prev is not None')
            node.getPrev().setNext(node.getNext())

        if node.getNext() is not None:
            print('Heree where next is not None')
            node.getNext().setPrev(node.getPrev())

        if node == self.head:
            self.head = node.getNext()

        if node == self.tail:
            self.tail = node.getPrev()

    def read(self, key):

        # Get the node from the hashtable
        nodeToRead = self.map.get(key, 'NOT_FOUND')
        if nodeToRead == 'NOT_FOUND':
            return None

        # Now remove the node from the linked list
        self.remove(key)

        # Add the node to the end of the LL
        self.addNode(nodeToRead.getKey(), nodeToRead.getValue())

        # Return the data that u wanna read
        return nodeToRead.getValue()

    def write(self, key, value):
        if len(self.map) == self.capacity:
            print('capacity full, deleting the oldest node')
            self.remove(self.head.getKey())
        else:
            print('capacity not full adding the latest')
        self.addNode(key, value)

    def remove(self, key):

        # Find the node from the hash table
        #print(self.map)
        print('key is - ', key)
        nodeToDelete = self.map.get(key, 'NOT_FOUND')
        if nodeToDelete == 'NOT_FOUND':
            print('Here node not found')
            return

        # remove the node from the linked list
        self.removeFromLinkedList(nodeToDelete)

        # remove the node from the map too
        self.map.pop(key)


n = int(input('Enter the size of array u want to put the elements - '))
capacity = int(input('Enter the capacity of LRU Cache - '))
arr = [[int(x) for x in input().split()] for y in range(n)]

LRU = LRUCache(capacity)

LRU.createLRUFromArray(arr)

print(LRU.map)

# operations to perform -
# Now do this - create a new node, and add it to the cache till the capacity gets full
node1 = Node(100, 'a')
node2 = Node(101, 'b')
node3 = Node(102, 'c')
node4 = Node(103, 'd')

LRU.addNode(node1.getKey(), node1.getValue())
LRU.addNode(node2.getKey(), node2.getValue())
LRU.printLL()

# Now the capacity is full, try to read it
LRU.read(100)
print('After Read 100 - ')
LRU.printLL()
LRU.read(1)
print('After Read 1- ')
LRU.printLL()
LRU.write(103, 'x')
print('After write new node ')
LRU.printLL()

