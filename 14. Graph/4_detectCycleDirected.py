
def detectCycleDirectedGraph(g, node):

    visited, ancestor = set(), set()

    def is_Cycle(node):

        visited.add(node)
        ancestor.add(node)

        # Loop through its neighbors
        for neighbor in g[node]:

            # Check if neighbor of node is ancestor, if yess
            # it is a backedge, return true
            if neighbor in ancestor:
                return True

            # Else check if neighbor is not in visited,
            # then we need to call recursively for the neighbor
            # And check if they return true
            elif neighbor not in visited:
                if is_Cycle(neighbor):
                    return True

        # if u reached till here, it means that there is no cycle, return False
        # We need to remove ancestors because for different edges, and vertices
        # Previous ancesrots does not make sense.
        ancestor.remove(node)
        return False

    # Loop through all the vertices in the graph
    for node in g.keys():
        if node not in visited:
            if is_Cycle(node):
                return True

    return False
