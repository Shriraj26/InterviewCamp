
"""

Get nth node in a Linked List
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def createLL(arr):
    head = None
    temp = None
    for i in arr:
        newNode = Node(i)
        if head is None:
            head = newNode
            temp = head
        else:
            temp.next = newNode
            temp = temp.next

    return head

def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def getNthNodeLL(head, n):

    temp = head
    for i in range(n-1):

        if temp is not None:
            temp = temp.next

    return temp

arr = [int(x) for x in input().split()]
n =  int(input('enter n '))
head = createLL(arr)

nthNode = getNthNodeLL(head, n)
printLL(nthNode)


