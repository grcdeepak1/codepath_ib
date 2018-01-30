class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A < 0:
            return 0
        if A <= 1:
            return 1
        paths = [1, 1]
        for i in range(2, A+1):
            count = paths[0] + paths[1]
            paths[0] = paths[1]
            paths[1] = count

        return count