"""
https://www.youtube.com/watch?v=ZyB_gQ8vqGA
Multiple things to consider and we will address one by one - 
1. We need all the tickets included in the result, pahile yaha jaa fir waha jaa fir yaya... 
   in lexicographical sorted order. therefore it is imp that we need a path..
2. It means that we need all the edges of the graph, with starting point JFK
3. First sort the input so that graph will be constructed with the choice for 
   dfs where to go next will be in lexicgraphical order.
4. THen construct the graph normally
5. You will stop in dfs when u know len(result) == len(edges) + 1 .. we include
    JFK as well.. edges = tickets
6. Another imp backtracking condition is that if u have a node that comes lexicgraphically
    before another node.. say in graph --
    A -> B, A-> C, and C-> A.. u will stop at node B.. then what? u need to backtrack
    and choose node C, then choose A then go to B.
7. As we traverse dfs, we keep on removing the neighbors from the node so that we
    dont visit them again and again..

"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Create nodes for source
        g = {src: [] for src, _ in tickets}

        # Sort the input
        tickets.sort()

        # Construct the graph
        for src, dest in tickets:
            g[src].append(dest)

        # Add JFK to the result
        result = ["JFK"]

        def dfs(src):

            if len(result) == len(tickets) + 1:
                return True

            # if no outgoing edge from the node, return False
            if g.get(src) is None:
                return False

            # Loop neighbors
            temp = list(g[src])
            for i, neighbor in enumerate(temp):

                # remove it from graph
                g[src].pop(i)
                # add it to result
                result.append(neighbor)

                # Recurse neighbor
                if dfs(neighbor):
                    return True

                # u reached till here means that there was no edge from
                # this neighbor, we need to unfollow this path, backtrack
                g[src].insert(i, neighbor)
                result.pop()

            # if u reached till here it means that dfs doesnt return true till here,
            # thus return False
            return False

        # Start dfs from JFK
        dfs("JFK")
        return result
