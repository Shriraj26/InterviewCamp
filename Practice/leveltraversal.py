class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelTraversal(root):

    q = []
    final = []
    q.append(root)

    while q:
        count = len(q)
        temp = []
        while count > 0:
            # pop front elem of the queueueueueueue!!!!!
            node = q.pop(0)
            print(node.data)
            temp.append(node.data)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

            count -= 1
        final.append(temp)

    print(final)

root = Node(3)
node9 = Node(9)
node20 = Node(20)
node15 = Node(15)
node7 = Node(7)

root.left = node9
root.right = node20
node20.left = node15
node20.right = node7

levelTraversal(root)


