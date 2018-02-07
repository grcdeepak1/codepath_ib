INF = float('inf')

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        ''' Compute minimum costs for each capacity '''

        MAX_C = 1000  # Given as constraint
        costs = [INF] * (MAX_C+1)
        for cap, cost in zip(B, C):
            costs[cap] = min(costs[cap], cost)

        for cap in range(2, MAX_C+1):
            for i in range(1, cap//2 + 1):
                costs[cap] = min(costs[cap], costs[i] + costs[cap-i])

        return sum(costs[cap] for cap in A)
