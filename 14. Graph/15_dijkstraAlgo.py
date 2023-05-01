import heapq


def dijkstra(g, src, dest):

    visited = set()
    dist = [float('inf') * len(g)]
    priQ = [(0, src)]
    visited.add(src)

    while priQ:

        # Get the current node and its current dist
        _, currNode = heapq.heappop(priQ)
        # Mark visited
        visited.add(currNode)

        # Loop neighbors
        for dest, destEdge in g[currNode]:

            if dest not in visited:

                # Update distances and push to heap
                if dist[dest] > destEdge + dist[currNode]:
                    dist[dest] = destEdge + dist[currNode]
                    heapq.heappush((dist[dest], dest))

    return dist
