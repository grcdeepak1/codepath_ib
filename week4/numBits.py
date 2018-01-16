class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if A <= 0:
            return 0
        elif A%2 == 0:
            return self.numSetBits(A/2)
        else:
            return (1 + self.numSetBits(A/2))