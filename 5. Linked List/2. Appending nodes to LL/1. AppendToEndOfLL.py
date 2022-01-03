"""
Given a node X, and head and tail pointers to a LL, append that node to its end

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


def getTail(head):
    if head is None:
        return None
    else:
        while head.next is not None:
            head = head.next

        return head


def append(head, tail, X):
    if head is None:
        return X
    else:
        tail.next = X
        tail = tail.next

    return head


arr = [int(x) for x in input().split()]
head = createLL(arr)
printLL(head)
tail = getTail(head)
print('tails ist - ')
printLL(tail)
print()

X = Node(int(input('enter the data for node u want to create -  ')))
head = append(head, tail, X)
printLL(head)
