"""
Smallest Subarray Covering All Values: Let's say you are given a large text document Doc. You are also given a set S of
words. You want to find the smallest substring of Doc that contains all the words in S.
For example:
S: ["and", "of", "one"]
Doc: "a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement,
question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses"
The underlined part above is the solution. Note that the order in which the words appear doesn't matter. Also, the length
of the substring is in terms of number of characters.

THis is a classic implementation of the LRU Cache!!
construct the LRU cache that has the set of words, the capacity will be that of the length of the array in set.
Whenever u encounter a word in the string that is in the SET, write to LRU cache the word and index where it was encountered...
Thus as u read on and on, u update/write to the LRU and their indices get updaed as well...
Maintain a min length where u will store the min length encountered till now, and then update it only when u
encounter a length lower than it...

"""
import sys

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

    # A Helper method to print the linked list
    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.key, temp.value, end=' -> ')
            temp = temp.next
        print()

    # Adds the node to the linked List
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
            node.getPrev().setNext(node.getNext())

        if node.getNext() is not None:
            node.getNext().setPrev(node.getPrev())

        if node == self.head:
            self.head = node.getNext()

        if node == self.tail:
            self.tail = node.getPrev()

    # This is a custom function that we will be using, this will check if node exists in hashtable, if yes,
    # delete it, and add a new node with the key and value given
    def writeUpdate(self, key, value):

        # get the node with the key provided
        nodeToDelete = self.map.get(key, 'NOT_FOUND')
        if nodeToDelete == 'NOT_FOUND':
            # add that node
            self.addNode(key, value)
        else:
            self.remove(key)
            self.addNode(key, value)


    def remove(self, key):

        # Find the node from the hash table
        nodeToDelete = self.map.get(key, 'NOT_FOUND')
        if nodeToDelete == 'NOT_FOUND':
            return

        # remove the node from the linked list
        self.removeFromLinkedList(nodeToDelete)

        # remove the node from the map too
        self.map.pop(key)

# we process the document as it is, until space appears, read it one by one, and then substring is the word from start till
# index where the space occurred, then process that substring...
def processDocument(LRU, S, rawDoc):

    # as u encounter a word in the document, if its in the Substring list, then add it to the LRU
    start = 0
    minLen = sys.maxsize
    for i in range(len(rawDoc)):

        if rawDoc[i] == ' ':
            subStr = rawDoc[start: i]

            # this methof does all the job
            minLen = operateSubString(subStr, start, LRU, S, minLen)

            # start is then incremented to again start from a new word after space
            start = i + 1

        # at the end of the document, inorder to include the last word, we are doing this...
        elif i == len(rawDoc) - 1:
            subStr = rawDoc[start: len(rawDoc)]
            minLen = operateSubString(subStr, start, LRU, S, minLen)

    print('The minimum length of such string  = ', minLen)

# This is the big daddy!!! it checks if substring from the document belongs to S, if yes we will add it to LRU, else proceed as it is
def operateSubString(substr, index, LRU, S, minLen):

    if substr in S:
        # then write it to the LRU
        LRU.writeUpdate(substr, index)

        LRU.printLL()

    # if the LRU is filled completely, keep on checking its first and last indices's for getting the length of substring
    # and update the minLen to get only the min len of the substring in doc where all the strings in S occur
    if len(LRU.map) == len(S):
        minLen = min(minLen, abs( (LRU.tail.getValue() + len(LRU.tail.getKey())) - LRU.head.getValue()))


    return minLen


print('Enter the string of characters for document - ')
rawDoc = input()
document = rawDoc.split()
print('enter the words whose substring u want to find out searated by spaces ')
S = [x for x in input().split()]

LRU = LRUCache(len(S))
processDocument(LRU, S, rawDoc)

