# While visiting vertices, if there exists a vertix that is part
# of both visited and recurStack set, then we have a cycle in a directed graph

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def isCyclicHelper(self, node, visited, recurStack):
        #visitNode
        #addToRecurStack
        visited.add(node)
        recurStack.add(node)

        #recurse
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.isCyclicHelper(neighbor, visited, recurStack):
                    return True
            elif neighbor in recurStack:
                return True

        #removeFromRecurStack
        recurStack.remove(node)
        return False

    def isCyclic(self):
        visited = set()
        recurStack = set()

        for node in range(self.V):
            if node not in visited:
                if self.isCyclicHelper(node, visited, recurStack):
                    return True
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)

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