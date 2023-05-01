"""
Main aim is to construct the graph with connections, 
See the code for details.. after that it is just checking - 
1. If cycle in directed graph, no topsort, no lexicographical order
2. Else return the topsort stack reverse
"""


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Add nodes to the graph
        g = {}
        for word in words:
            for c in word:
                if g.get(c) is None:
                    g[c] = []

        # Add edges to the graph
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            # Check if word1 > word2 and word1 till len of word2 is == word2
            # Eg - wrtg wrt ---> in this, we return "" as g in front doesnt mean anything
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            # Iterate for min len out of w1 or w2
            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                if w1[j] != w2[j]:
                    # Edge from w1 to w2
                    g[w1[j]].append(w2[j])

                    # This is a very important condition to note!!
                    # Consider example - ab bc --- in this u say that a -> b graph
                    # Then u need to stop as u still dont know priority of
                    # b and c that are the next letters in the graph
                    break

        # Preparing for topsort dfs!!
        visited = set()
        ancestor = set()
        stack = []

        def topSortDetectCycle(node):
            visited.add(node)
            ancestor.add(node)
            for neighbor in g[node]:
                if neighbor not in visited:
                    if topSortDetectCycle(neighbor):
                        return True
                elif neighbor in ancestor:
                    return True
            ancestor.remove(node)
            stack.append(node)
            return False

        # Call topsort for every node in the graph that is not visited yet
        for node in g.keys():
            if node not in visited:
                if topSortDetectCycle(node):
                    return ""

        # Return the string by joing the stack in reverse
        return "".join(stack[::-1])
