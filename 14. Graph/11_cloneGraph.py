"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
You will need a map for mapping old nodes to new nodes
Create copy of root node, add to dict
Get the rootCopy
Loop through neighbors of root, if neighborCopy does not exist, create it
Attach neighbor copy to the root copy
Then recurse
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # If node is None, return None
        if not (node):
            return None

        # Store the current node and its copy
        myDict = {node: Node(node.val, None)}
        visited = set()

        def dfsHelper(node):

            visited.add(node)

            # Get the copy of current node in dict
            nodeCopy = myDict[node]

            for neighbor in node.neighbors:

                # Create neighbor copy if not in dict
                if myDict.get(neighbor) is None:
                    neighborCopy = Node(neighbor.val, None)
                    myDict[neighbor] = neighborCopy

                # Get the neighbor copy
                neighborCopy = myDict[neighbor]

                # Add the neighbor copy to the node copy
                nodeCopy.neighbors.append(neighborCopy)

                # Recurse
                if neighbor not in visited:
                    dfsHelper(neighbor)

        dfsHelper(node)

        return myDict[node]
