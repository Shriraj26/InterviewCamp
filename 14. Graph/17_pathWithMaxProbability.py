"""
This is just dijkhstra with some modifications like- 
1. Mantain a max heap for storing max dist towards the node, this will be probabilities
2. the distance calculation will have multiplication as the question jutifies
3. return the distance till the end dest
"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        # Construct the graph
        g = {i: [] for i in range(n)}
        for i, (src, dest) in enumerate(edges):
            g[src].append([dest, succProb[i]])
            g[dest].append([src, succProb[i]])

        # Dijkstra
        visited = set()
        # -1 dist for current source as it is a max heap so nevagive and 1 for multiplication easiness
        priQ = [(-1, start)]
        # dist array
        dist = [-float('inf')] * len(g)
        # current source ka dist 1 mark kar de
        dist[start] = 1

        while priQ:

            # pop from pri q, prpcess then mark visited
            _, currNode = heapq.heappop(priQ)
            visited.add(currNode)

            # loop neighbors
            for dest, destWeight in g[currNode]:
                if dest not in visited:

                    # Most imp condition in Dijkstra modified!!
                    if dist[dest] < destWeight * dist[currNode]:
                        dist[dest] = destWeight * dist[currNode]
                        # after updating then only push in the priq
                        heapq.heappush(priQ, (-dist[dest], dest))

        if dist[end] == -float('inf'):
            return 0
        return dist[end]
