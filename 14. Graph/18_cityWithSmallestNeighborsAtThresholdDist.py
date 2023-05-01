"""
Apply dijkstra from every node, but explore its neuighbor only when dist[currNode] + weight of neighbor < threshold
For every node, in the dist array count the cities within the threshold
"""

import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # Graph construction
        g = {i: [] for i in range(n)}
        for src, dest, weight in edges:
            g[src].append([dest, weight])
            g[dest].append([src, weight])

        # this will return number of cities reachable from src within that threshold
        def dijkstra(src) -> int:

            visited = set()
            dist = [float('inf')] * len(g)
            dist[src] = 0
            djPriQ = [(0, src)]

            while djPriQ:

                _, currNode = heapq.heappop(djPriQ)
                visited.add(currNode)

                # loop neighbors and imp conition
                for dest, destweight in g[currNode]:

                    if dest not in visited:
                        if dist[currNode] + destweight > distanceThreshold:
                            # print('Here ')
                            continue

                        if dist[dest] > destweight + dist[currNode]:
                            dist[dest] = destweight + dist[currNode]
                            heapq.heappush(djPriQ, (dist[dest], dest))

            # Count the cities that are reachable except the source
            count = 0
            for i in range(len(dist)):
                if i != src and dist[i] != float('inf'):
                    count += 1

            return count

        # Count the cities with min number of reachable cities and simultaneously count the max value for that city
        minNumCities, maxCity = float('inf'), -float('inf')
        for node in g.keys():
            numCities = dijkstra(node)

            if minNumCities >= numCities:
                if maxCity < node:
                    maxCity = node
                minNumCities = numCities

        # print(minNumCities, maxCity)

        return maxCity
