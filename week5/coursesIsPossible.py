from collections import defaultdict
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer

    def isCyclic(self, node, g, visited, recurStack):
        visited.add(node)
        recurStack.append(node)

        for neighbor in g[node]:
            if neighbor not in visited:
                if self.isCyclic(neighbor, g, visited, recurStack):
                    return True
            elif neighbor in recurStack:
                return True

        recurStack.pop()
        return False

    def isPossible(self, g, A):
        visited = set()
        recurStack = []
        for node in range(1, A):
            if node not in visited:
                if self.isCyclic(node, g, visited, recurStack):
                    return 0
        return 1

    def solve(self, A, B, C):
        g = defaultdict(list)
        for b,c in zip(B,C):
            g[c].append(b)

        return self.isPossible(g, A)