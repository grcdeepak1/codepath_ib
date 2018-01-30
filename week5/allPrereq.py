from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.indegree = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    #ans - keeps track of 1 order
    #sol - list of ans (all orders of topo sort)
    def allTopoSort(self, visited, ans, sol):
        flag = False

        for v in range(self.V):
            #only choose vertices with indegree 0 and not visited
            if self.indegree[v] == 0 and v not in visited:
                #reduce indegree of neighbor
                for neighbor in self.graph[v]:
                    self.indegree[neighbor] -= 1
                ans.append(v)
                visited.add(v)

                #explore
                self.allTopoSort(visited, ans, sol)

                #reset indegree of neighbor
                visited.remove(v)
                ans.pop()
                for neighbor in self.graph[v]:
                    self.indegree[neighbor] += 1
                flag = True

        if flag != True:
            sol.append(ans[:])

    def allPrereq(self):
        visited = set()
        sol = []
        self.allTopoSort(visited, [], sol)
        return sol


    def dfs(self, course, graph, visited, ans):
        visited.add(course)

        for dependent in graph[course]:
            if dependent not in visited:
                self.dfs(dependent, graph, visited, ans)

        ans.append(course)


    def prereq(self):
        courses = self.V
        n       = courses
        graph   = self.graph
        visited = set()
        ans = []
        for c in reversed(range(courses)):
            if c not in visited:
                print(c)
                self.dfs(c, graph, visited, ans)
        return ans

g = Graph(4)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(3, 1)
g.addEdge(3, 2)
print(g.allPrereq())