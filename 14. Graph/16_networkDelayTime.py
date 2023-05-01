"""
Mrking visited is the most imp thing i noticed, after u pop from pri q, then mark it as visited
Just when u process the node, then u mark it as visited.. this is exactly like that...
"""

import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, source: int) -> int:

        # Construct the graph
        g = {i+1: [] for i in range(n)}
        for src, dest, weight in times:
            g[src].append([dest, weight])

        # Dijkstra
        visited = set()
        # Add 0 dist for current source
        priQ = [(0, source)]
        # dist array with size + 1 because nodes start from 1 and not 0
        dist = [float('inf')] * (len(g)+1)
        # current source ka dist 0 mark kar de
        dist[source] = 0

        while priQ:

            # pop from pri q
            _, currNode = heapq.heappop(priQ)

            if currNode in visited:
                continue

            visited.add(currNode)

            # loop neighbors
            for dest, destWeight in g[currNode]:

                if dest not in visited:

                    # Most imp condition in Dijkstra!!
                    if dist[dest] > destWeight + dist[currNode]:
                        dist[dest] = destWeight + dist[currNode]
                        # after updating then only push in the priq
                        heapq.heappush(priQ, (dist[dest], dest))

        # as 0 index stores inf
        minTime = max(dist[1:])
        if minTime != float('inf'):
            return minTime

        return -1
