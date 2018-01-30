#Idea : BFS 1 from any node to last node, return (node, distance)
#BFS 2 using the returned node will give u the largest distance and the other node

from collections import defaultdict
from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer

    def buildGraph(self, A):
        g = defaultdict(list)
        for i,n in enumerate(A):
            if n != -1:
                g[n].append(i)
                g[i].append(n)
        return g

    def bfs(self, u, g, n):
        nodesToVisit = deque([u])
        visited = set()
        dis = [-1]*n

        dis[u] = 0
        while len(nodesToVisit) > 0:
            t = nodesToVisit.popleft()
            if t in visited:
                continue
            visited.add(t)

            for v in g[t]:
                if v not in visited:
                    dis[v] = dis[t] + 1
                    nodesToVisit.append(v)

        return (dis.index(max(dis)), max(dis))


    def solve(self, A):
        g = self.buildGraph(A)
        node1, distance1 = self.bfs(0, g, len(A))
        node2, distance2 = self.bfs(node1, g, len(A))
        return distance2