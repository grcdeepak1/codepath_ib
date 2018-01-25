# While visiting vertices, if there exists a neighbor of a vertex that is part
# of both visited set and not a parent of the vertex, then we have a cycle in an undirected graph

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def isCyclicHelper(self, node, visited, parent):
        #visitNode
        visited.add(node)

        #recurse
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.isCyclicHelper(neighbor, visited, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    def isCyclic(self):
        visited = set()
        for node in range(self.V):
            if node not in visited:
                if self.isCyclicHelper(node, visited, -1):
                    return True
        return False


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(2, 4)
g.addEdge(4, 2)
g.addEdge(3, 4)
g.addEdge(4, 3)

# g = Graph(5)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(3, 2)
# g.addEdge(4, 3)
# g.addEdge(4, 1)

# print(g.graph)
# print(g.V)

print(g.isCyclic())